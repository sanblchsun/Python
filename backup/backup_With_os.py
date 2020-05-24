# coding:utf8
# создание архива директории  с помощью модуля zipfile
#--------------------------------------------------------------------
 
import os
import time
import zipfile
 
# Директория для создания архива
source=input('Укажите файл для упаковки в zip архив -->')
 
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir ='E:\\BACKUP' # Подставьте тот путь, который вы будете использовать.
 
# Создаём каталог, если его ещё нет
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # создание каталога
    print('Каталог успешно создан', target_dir)
 
# 3. Файлы помещаются в zip-архив.
 
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
 
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
 
# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
comment.replace(' ', '_') + '.zip'
 
# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)
 
zipp=zipfile.ZipFile(target,mode='w')# создание архива
for root, dirs, files in os.walk(source):# получаем адрес каталога и имена подкатологов и файлов 
   for file in files:
        zipp.write(os.path.join(root,file))# пишем файлы в архив
        
zipp.close()