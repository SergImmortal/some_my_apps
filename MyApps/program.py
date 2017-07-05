from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import urllib.request, time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request, urllib.error, csv, time, random, time, asyncio, os, xlrd

def get_user_agent():
    useragent=[]
    usag = urllib.request.urlopen("http://willdrevo.com/public/text/user_agents.txt").read()
    with open ("user_agent.doc", "wb") as f:
        f.write(usag)
        f.close()
    f = open("user_agent.doc", "r")
    for line in f.readlines():
        useragent.append(line[1: len(line)-2])
    f.close()
    return useragent[int(random.uniform(1,(len(useragent))))]

my_list =()  # сюда закинь какой-то список видео

def click_youtube():
    for i in range(0,1000):      
        opts = Options()
        opts.add_argument("user-agent="+get_user_agent())
        driver = webdriver.Chrome(chrome_options=opts)
        driver.implicitly_wait(random.randint(20, 25))
        driver.get(my_list[(random.randint(0,len(my_list)-1))])
        driver.set_window_size(100, 100)
        link1 = driver.find_elements_by_id('adContent-clickOverlay')
        driver.quit()
click_youtube()

