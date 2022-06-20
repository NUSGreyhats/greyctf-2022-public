# SelNode

### Challenge Details
hosting a selenium node([https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar))](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)) on a clean linux, players need to read the contents of the file on the server. 

### Key Concepts
browser tricks to read local files.

### Solution

connect to selenium node and ask browser to visit `file:///etc/passwd` will read the contents of `/etc/passwd`, but the same trick can't be used to read the contents of `/flag` because it's a binary file(or at least I can't directly read it)

need to use the [FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader) js api to read the contents of the file and return back. refer to https://github.com/JonStratton/selenium-node-takeover-kit/blob/master/examples/selenium_node_download.py or [sol.py](./sol.py) to download the `/flag` binary and run it to get the flag.


### Learning Objectives
same as Key Concept

### Flag
```
grey{publ1c_53l3n1um_n0d3_15_50_d4n63r0u5_8609b8f4caa2c513}
```

