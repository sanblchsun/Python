import time

text = '''
		В пункте except мы указываем класс ошибки 
		ShortInputException, который будет сохранён
		как[3] переменная ex, содержащая соответствующий 
		объект ошибки/исключения. Это аналогично параметрам
		и аргументам при вызове функции.
		Внутри этого пункта except мы используем поля length и
		atleast объекта исключения для вывода необходимых 
		сообщений пользователю.'''

fw = open('mytest.txt', 'w')
fw.write(text)
fw.close()

try:
	fr = open('mytest.txt')
	while True:
		line = fr.readline()
		if len(line)==0:
			break
		print(line, end=' ')
		time.sleep(2)
except KeyboardInterrupt:
	print('Чтение файла было прервано')
finally:
	fr.close()
	print('\nФайл закрыт')