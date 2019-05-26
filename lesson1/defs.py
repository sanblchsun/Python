def cena(rub, kop=0):
  return "%i руб. %i коп." % (rub, kop)

print (cena(8, 50))
print (cena(7))
print (cena(rub=23, kop=70))
