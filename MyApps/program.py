from selenium import webdriver
import random
import time
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def statusbar(x, y):
    r = (y/x)*100
    r = round(r, 2)
    return r

def statistic(k, l, count):
    res1 = str(statusbar(l, count)) + ' %'  
    res2 = str(k) + ' Просмотров'
    return res1, res2

def ipfilter(ip, iplist):
    res = True
    for i in iplist:
        if ip == i:
            res = False
            break
    return res
    
def validationip():
    driver.set_window_size(100, 100)
    driver.get('http://www.showmyip.gr/')
    ipconf = driver.find_element_by_class_name('ip_address')
    ip = ipconf.text
    res = ipfilter(ip, usediplist)  
    usediplist.append(ip)
    return res

count = 0
k = 0
usediplist = []
name = "Not so fast"
dict = {'Как сделать арбузный сок / My Watermelon Juice': ['Как сделать арбузный сок not so fast', 'My Watermelon Juice not so fast', 'Как сделать арбузный сок / My Watermelon Juice'], 
        'Kinetic Sand / Кинетический песок': ['Kinetic Sand / Кинетический песок', 'Kinetic Sand not so fast', 'Кинетический песок not so fast'], 
        'Крахмал и вода - неньтоновская жидкость/ Non-Newtonian fluid': ['Крахмал и вода - неньтоновская жидкость/ Non-Newtonian fluid', 'Крахмал и вода - неньтоновская жидкость not so fast', 'Non-Newtonian fluid not so fast']}
d = dict
l = 1000 #int(input('Введите  количество цыклов: '))
for c in range(0, l):
    key = d.keys()
    z = []
    for i in key:
        z.append(i)
    namevideo = str(random.choice(z))
    a = d.get(namevideo)
    a = int(len(a))
    serchtext = (d[namevideo][random.randint(0, a-1)])
    try:
        with TorBrowserDriver("/home/serj/selenium/tor-browser_en-US") as driver:
            res = validationip()
            if res == True:
                driver.set_window_size(1300, 760)
                driver.get('https://www.youtube.com/')
            else:
                driver.close
            time.sleep(random.randint(2, 5))
            try:
                serch = driver.find_element_by_id('masthead-search-term')
                serch.send_keys(serchtext)
                klikforserch = driver.find_element_by_id('search-btn')
                time.sleep(random.randint(2, 7))
                klikforserch.click()
                serchvideo = driver.find_element_by_link_text(namevideo)
                driver.implicitly_wait(20)
                time.sleep(random.randint(2, 7))
                serchvideo.click()
                time.sleep(random.randint(20, 70))
                k += 1
                for g in range(0, random.randint(2, 5)):
                    try:
                        linksss = driver.find_elements_by_xpath("//*[@class='g-hovercard']")
                        for i in linksss:
                            if i.text == name:
                                k += 1
                                i.click()
                                time.sleep(random.randint(20, 70))
                    except:
                        rf = 0
            except:
                print('Ошибка загрузки страницы')
            driver.close()
        count += 1
        print(statistic(k, l, count))
    except:
        print('Ошибка загрузки или закрытия вебдрайвера')
