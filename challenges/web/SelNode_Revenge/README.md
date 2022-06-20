# SelNode_Revenge

### Challenge Details
harder version of SelNode. Players need to get RCE(reverse shell) on that service, and execute `/flag` to get flag. only chrome will be installed on the system, to prevent user getting RCE by abusing the [Firefox Profile specifying custom handler](https://github.com/JonStratton/selenium-node-takeover-kit/blob/master/examples/selenium_node_rce.rb).

### Key Concepts
online references([https://nutcrackerssecurity.github.io/selenium.html](https://nutcrackerssecurity.github.io/selenium.html) and [https://twitter.com/yarlob/status/1189303557109014534](https://twitter.com/yarlob/status/1189303557109014534)) only give a PoC for popping a calculator on the windows target system. But achieving RCE for arbitrary command is not trivial on Linux. `--utility-cmd-prefix` is being processed by [CommandLine::PrependWrapper](https://source.chromium.org/chromium/chromium/src/+/main:base/command_line.cc;drc=1ed3995c6899fba1326b8543833b97a16a22dc5e;bpv=1;bpt=1;l=455?q=utility-cmd-prefix&ss=chromium&gsn=PrependWrapper&gs=kythe%3A%2F%2Fchromium.googlesource.com%2Fchromium%2Fsrc%3Flang%3Dc%252B%252B%3Fpath%3Dsrc%2Fbase%2Fcommand_line.h%23_7A0IDBP3kB1J61HP8VGGUrWoHDItIn-yq24PQf8tHU&gs=kythe%3A%2F%2Fchromium.googlesource.com%2Fchromium%2Fsrc%3Flang%3Dc%252B%252B%3Fpath%3Dsrc%2Fbase%2Fcommand_line.cc%23uA__1Ad7GrcbTKM2W69Q_j9K3M_UH3HCrWN_P7_lak4), and selenium node is escaping backslash `/` into `\u002f`

### Solution

refer to [sol.py](./sol.py)


### Learning Objectives
set up ur own environment and do the debugging.

### Flag
```
grey{y0u_4r3_qu4l1f13d_45_r34l_h4ck3r_68c620210bd61385}
```

