#!/usr/bin/python3
print("Ultimate Checker 4.0")
print("You can enter your answer in any order (the checker is smart enough)")

a = float(input("#1: "))
b = float(input("#2: "))
c = float(input("#3: "))

ans = [a, b, c]
ans.sort()

print("Initializing super high precision checker. This will take around 5 seconds.")

import time
time.sleep(5)

actual = [-12.325308285692675, 1.9802198205222012, 15.143309061102336]
delta = 0
for x, y in zip(ans, actual):
  delta += abs(x - y)

flag = "grey{3m_iS_bL4cK_mAg1C}"
if delta < 0.05:
  print(f"Here is your flag: {flag}")
else:
  print("Failed: total error not within 0.05")
