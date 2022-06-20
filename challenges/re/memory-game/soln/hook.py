import frida
import time
device = frida.get_usb_device()
pid = device.spawn(["com.snatik.matches"])
device.resume(pid)
time.sleep(1) #Without it Java.perform silently fails
session = device.attach(pid)
script = session.create_script(open("hook.js").read())
script.load()

#prevent the python script from terminating
input()
