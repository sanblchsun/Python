from dict_pickly import ClassRules

obj = ClassRules()


def func_key(name_last='', name_first='', name_middle=''):
    '''Это функция - шаблон
    что бы создавать ключа для типа данных справочник.
    Для заполнения праметров функции испроользуйте правило:
    func_key(
        name_first='Петр',
        name_middle='Петрович',
        name_last='Петров')
    в этом случае параметры являются именованными и
    указываться могут в любом порядке'''

    return (name_last, name_first, name_middle)


dict_data = {func_key(
    name_first='Петр',
    name_middle='Петрович',
    name_last='Петров'): {
    'address': [
        'г. Москва', 'ул. Ленина', 'д.1', 'кв.10'],
    'email':
        'test@ftest.ru',
    'phone': {
        'home_phone': '25-66-44',
        'mobile_phone1': '8-925-111-11-11',
        'mobile_phone2': ''}}}

obj.add_data(dict_data)

mydict = obj.get_data()

print(mydict[func_key(
    name_first='Петр',
    name_middle='Петрович',
    name_last='Петров')])
