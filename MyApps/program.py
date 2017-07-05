from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import urllib.request, time
from urllib.request import Request, urlopen
import urllib.request, urllib.error, time, random, time, asyncio, os

useragent=[]
usag = urllib.request.urlopen("http://willdrevo.com/public/text/user_agents.txt").read()
with open ("user_agent.doc", "wb") as f:
    f.write(usag)
    f.close()
f = open("user_agent.doc", "r")
for line in f.readlines():
    useragent.append(line[1: len(line)-2])
    f.close()
for i in range(0,1000): 
    g = str(random.choice(useragent))
    print(g)    
    opts = Options()
    opts.add_argument("user-agent="+ g)
    driver = webdriver.Chrome('/usr/bin/google-chrome-stable')
    driver.implicitly_wait(random.randint(20, 25))
    driver.get('http://browser-info.ru/')
#   driver.set_window_size(100, 100)
    link1 = driver.find_elements_by_id('adContent-clickOverlay')
    driver.quit()
