try:
    res = int(open('a.txt').read())/int(open('b.txt').read())
    print (res)
except IOError:
    print("шибка ввода- вывода")
except ArithmeticError:
    print("Деление на 0")
except KeyboardInterrupt:
    print ("Прерывание с клавиатуры")
except ValueError:
    print("Не числовое значение: ")        
except:
    print("Неизвестная ошибка")
    
