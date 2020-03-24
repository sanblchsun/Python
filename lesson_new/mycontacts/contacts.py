import pickle



dist_contacts =\
 {('Иванов', 'Иван', 'Иванович'):('test@test.ru', 'Moskva', 29)}
f = open('./file_data.data', 'wb')
pickle.dump(dist_contacts, f)
f.close()


dist_contacts[('Семенов', 'Семен', 'Семенович')] =\
 				('test1@test.ru', 'Moskva', 40)
print(dist_contacts['Иванов', 'Иван', 'Иванович'][0])
for key in dist_contacts.keys(): print(key)