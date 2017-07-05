import random

"""
функция считает процент исполнения задания программы
принимает x - заданное количество просмотров y - выполненое количество просмотров
возвращает процент исполнения
"""
def statusbar(x, y):
	r = (y/x)*100
	r = round(r, 2)
	return r
"""
Функция считает реальные (завершонные) просмотры
принимает k - счетчик просмотров, l - заданное количество просмотров, count - количество выполненных циклов
Возвращает оформленное количество просмотров + процент выплнения цыклов в %
использует функцию statusbar()
"""
def statistic(k, l, count):
	res1 = str(statusbar(l, count)) + ' %'	
	res2 = str(k) + ' Просмотров'
	return res1, res2
"""
Функция отсекает повторяющиеся ip в 1 сессии(!!!слабая сторона!!!)
принимает ip - адрес со страницы айпичекара, iplist список который нужно хранить всю сессию(глобальная переменная)
Возвращает True или False
"""
def ipfilter(ip, iplist):
	res = True
	for i in iplist:
		if ip == i:
			res = False
			break
	return res
"""
Заходит на сайт ip чекера получает адрес и с помащью функции ipfilter() отсеивает повторняющиеся.
принимает driver - ну как бы понятно, usediplist - лист использованных адресов(глобальная переменная)
Возвращает True или False
"""	
def validationip(driver, usediplist):
	driver.set_window_size(100, 100)
	driver.get('http://www.showmyip.gr/')
	ipconf = driver.find_element_by_class_name('ip_address')
	ip = ipconf.text
	res = ipfilter(ip, usediplist)	
	usediplist.append(ip)
	return res
"""
Функция выберате случайное название видео и выберает случайный запрос к видео из созданного ранее словаря
принимает d - словарь
Возвращает namevideo - имя видео по которому будет кликать, serchtext - текст запроса для поиска видео
"""
def serchrequest(d):
	key = d.keys()
	z = []
	for i in key:
		z.append(i)
	namevideo = str(random.choice(z))
	a = d.get(namevideo)
	a = int(len(a))
	serchtext = (d[namevideo][random.randint(0, a-1)])
	return namevideo, serchtext
"""
Функция ищет елементы страницы с заданым именем канала и сохраняет их в список
получает driver - понятно, xpath - путь к искомому элементу в котором выводятся ремомендуемые видео,
 name - имя канала
возвращает list - список елементов страницы и имям канала
"""
def validlinklist(driver, xpath, name):
	list = []
	links_in_list = driver.find_elements_by_xpath("//*[@class='g-hovercard']")
	for i in links_in_list:
		if i.text == name:
			list.append(i)
	return list	
"""
Функция выберат рандомный элемент, ищет позицию елемента и выдает елемент
принимает linklist - список отфильтрованных видео функцией validlinklist()
возвращает position - позиция элемента по оси Y, link - обьект позиция которого определена, 
"""	
def finde_position(linklist):
	link = random.choice(linklist)
	height = link.location
	key = height.keys()
	for i in key:
		if i == 'y':
			y = str(i)
			break
	position = str(height.get(y) - random.randint(90, 130))
	return position, link
