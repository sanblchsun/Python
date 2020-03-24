import time
from pathlib import Path
from zipfile import ZipFile

# каталоги, которые копируем, собираются в список
srcs = [Path('/') / 'home' / 'sun' / 'Downloads' / '1',
		Path.home() / 'Downloads' / '2']

# куда будем сохранять backup
targer_dir = Path.home() / 'backup_temp'

# каталог для бэкапа на сегодня
today = targer_dir / time.strftime('%Y_%m_%d')

#Сделаем проверку на анличие каталога 		для копирования, если его нет создадипм его
if not Path.exists(today):
	today.mkdir(parents=True) # делаем каталог, если его еще нет
	print('Каталог успешно создан : ', today)

# запрашиваем коментарии пользователя для именя файла
comment = input('Введите комментарии: ').strip().replace(' ', '_')

# это имя файла с текущим временем и включенными комментариями
name_backup = time.strftime('%H_%M_%S_') + '{}.zip'.format(comment)

# полный путь к zip - файлу
target = str(today / name_backup)

zipp=ZipFile(target,mode='w')# создание архива

extension = "*.*" # тут указать шаблон для фильтации

for src in srcs:	
	for filenameFull in src.rglob(f"{extension}"):
		zipp.write(filenameFull)# пишем файлы в архив
        
zipp.close() # закрываем архив