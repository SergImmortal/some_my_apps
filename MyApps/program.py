import os
import random
from selenium import webdriver
from collections import Counter
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.support.ui import WebDriverWait

# Обьявляем элементы
array = []
urllist = []
print('---***Вас приветствует програмка NAVRATIL***---\n')
print('Программа создана просмативать заданное количество страниц на YouTube \n заданное количество раз заходя под разными ip адресом \n')
# Создаем список страниц
while True:
    comand = str(input('Введите адрес страницы или "start" для начала DDos атаки: '))
    if comand == 'start':
        print('В список добавлены следующие ссылки: \n%s.' % ', \n'.join(urllist))
        break
    else:
        urllist.append(comand)
    print('Добавлено в список')
# Воодим остальные данные
q = int(input('Введите количество просмотров для всех страниц: '))
time = int(input('Введите время просмотра на страницы: ' )) 
#Начинаем цикл 
for i in range(0, q):
    with TorBrowserDriver("/home/serj/selenium/tor-browser_en-US/") as driver:
        driver.set_window_size(100, 100)
        random.shuffle(urllist)
        for i in urllist:
            driver.get(i)
            try:
                titleserch = driver.find_element_by_id('eow-title')
                title = titleserch.text
                array.append(title)
                realtime = str(time + random.randint(1, 15)) # рандомим время
                driver.implicitly_wait(realtime) # Ждем
                link1 = driver.find_elements_by_id('adContent-clickOverlay')
                print('Выполнение ' + str (i/q*100) + ' % ' + ' Просмотр страницы - '+ str(title)+ ' - ' + str(realtime)+ 'сек.') #Результат ожидания
            except:
                print('Oшибка')
        driver.close() #И заново
#Выводим статистику
print('DDoS атака завершена \n ')
abc = Counter(array)
for key, value in abc.items():
        print('Страница "' + str(key) + '"Ы просмотров ' + str(value))
