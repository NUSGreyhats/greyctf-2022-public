# Quotes

### Challenge Details
a challenge testing on [cross-site websocket hijacking](https://book.hacktricks.xyz/pentesting-web/cross-site-websocket-hijacking-cswsh), user can get the different quotes via websocket api, only request coming from `http://localhost.*`(this is flawed)  with correct cookie can get the flag as quote. cookie was set via `/auth` endpoint, served for localhost only. user can also share a quote to the admin by sending a url for the bot to visit.

### Key Concepts
- websocket
- cross-site websocket hijacking
- same-site cookie
- different same-site cookie policy between firefox and chrome

### Solution
User can perform cross-site websocket hijacking by providing admin a malicious page(hosting on http://localhost.xxxxxx.yyy/test.html), which visit `/auth` first to get cookie set, and then get the flag quote from the websocket api endpoint when cookie was brought along. See [exp.html](./exp.html) for sample implementation.

### Learning Objectives
same as key concept

### Flag
grey{qu0735_fr0m_7h3_w153_15_w153_qu0735_7a4c6ec974b6d8b0}