import decimal
d = decimal.Decimal('3.456')
print(d + 1)

decimal.getcontext().prec = 4
print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))