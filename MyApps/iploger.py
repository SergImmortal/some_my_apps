import os
from selenium import webdriver
from collections import Counter
from tbselenium.tbdriver import TorBrowserDriver
import pickle 


na_file = open('/home/serj/python/tor_ip', 'wb')
array = []
i = 0
q = 100
while i < q:
	with TorBrowserDriver("/home/serj/selenium/tor-browser_en-US/") as driver:
		driver.get('https://2ip.ru/')
		ipconf = driver.find_element_by_id('d_clip_button')
		ip = ipconf.text
		array.append(ip)
		driver.quit()
		i +=1
		print(str(i/q*100) + ' %')
abc = Counter(array)

pickle.dump(abc, na_file)
na_file.close()

print(abc)
