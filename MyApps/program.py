from mymodul import *
from selenium import webdriver
import random
import time
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
""" Введеие всех  стартовых переменных """
usediplist = []
count = 0
k = 0
name = "Not so fast"
xpath = "//*[@class='g-hovercard']"
dict = {'Как сделать арбузный сок / My Watermelon Juice': ['Как сделать арбузный сок not so fast', 'My Watermelon Juice not so fast', 'Как сделать арбузный сок / My Watermelon Juice'], 
        'Kinetic Sand / Кинетический песок': ['Kinetic Sand / Кинетический песок', 'Kinetic Sand not so fast', 'Кинетический песок not so fast'], 
        'Крахмал и вода - неньтоновская жидкость/ Non-Newtonian fluid': ['Крахмал и вода - неньтоновская жидкость/ Non-Newtonian fluid', 'Крахмал и вода - неньтоновская жидкость not so fast', 'Non-Newtonian fluid not so fast']}
d = dict
l = 1000
""" Запускаем щикл колическтва поисковых запросов """
for c in range(0, l):
    namevideo, serchtext = serchrequest(d) #функция случайного выбора видео и случайного поискового запроса к нему из словаря
    try:
        with TorBrowserDriver("/home/serj/selenium/tor-browser_en-US") as driver:
            res = validationip(driver, usediplist) #функция сравнения ИП с уже использованными
            if res == True:
                driver.set_window_size(1366, 768)
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
                time.sleep(random.randint(5, 7))
                serchvideo = driver.find_element_by_link_text(namevideo)
                driver.implicitly_wait(20)
                time.sleep(random.randint(2, 7))
                serchvideo.click()
                time.sleep(random.randint(20, 70))
                k += 1
                for g in range(0, random.randint(2, 5)):
                    try:
                        time.sleep(random.randint(10, 15))
                        trulinks = validlinklist(driver, xpath, name) #функция выберающая видео заданного канала из рекомендованых          
                        k += 1
                        position, link = finde_position(trulinks) # Определяем координаты и обьект по которому клацнем
                        skrollposition = 'window.scrollTo(0, '+ position +');' #надосделать строкой, это пердается в JS
                        driver.execute_script(skrollposition)
                        time.sleep(random.randint(10, 12))
                        link.click()
                    except:
                        rf = 0
            except:
                print('Ошибка загрузки страницы')
            driver.close()
        count += 1
        print(statistic(k, l, count)) # функция счетчика просмотров
    except:
        print('Ошибка загрузки или закрытия вебдрайвера')
