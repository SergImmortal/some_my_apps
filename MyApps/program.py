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

def listcreate():
    urllist = []
    # Создаем список страниц
    while True:
        comand = str(input('Введите несколько поисковых запросов или start для начала: '))
        if comand == 'start':
            print('В список добавлены следующие запросы: \n%s.' % ', \n'.join(urllist))
            break
        else:
            urllist.append(comand)
            print('Добавлено в список')
    return urllist
"""
Поисковые запрос:
my watermelon juice not so fast - накрылся
not so fast my watermelon juice -накрылся
как сделать арбузный сок / fast - накрылся
fast как сделать арбузный сок  +
fast 100% арбузный сок +
100% so fast watermelon juice - накрылся
"""

def statistic(k, l, count):
    res1 = str(statusbar(l, count)) + ' %'  
    res2 = str(k) + ' Просмотров'
    return res1, res2

count = 0
k = 0
name = "Not so fast" #str(input('Введите  назване канала: '))
serchtext = listcreate()
namevideo = "Как сделать арбузный сок / My Watermelon Juice"  #str(input('Введите  имя видео: '))
l = 3000 #int(input('Введите  количество цыклов: '))
for c in range(0, l):
    try:
        with TorBrowserDriver("/home/serg/selenium/tor-browser_en-US") as driver:
            driver.get('https://www.youtube.com/')
            time.sleep(random.randint(2, 5))
            try:
                serch = driver.find_element_by_id('masthead-search-term')
                serch.send_keys(str(random.choice(serchtext)))
                klikforserch = driver.find_element_by_id('search-btn')
                time.sleep(random.randint(2, 7))
                klikforserch.click()
                serchvideo = driver.find_element_by_link_text(namevideo)
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