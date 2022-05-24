
duration = int(input('Введите положительное число '))
d = 0
s = duration % (24 * 3600)
h = s // 3600
s %= 3600
m = s // 60
s %= 60

if duration >= 86400:
    d = duration // 86400

print(f'{d} дней {h} часов  {m} минут {s} секунд ' )







