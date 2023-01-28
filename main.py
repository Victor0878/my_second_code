per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
val_per = list(per_cent.values())
t, s,  v, sb = val_per[0], val_per[1], val_per[2], val_per[3]
t = int(val_per[0]*money / 100)
s = int(val_per[1]*money / 100)
v = int(val_per[2]*money / 100)
sb = int(val_per[3]*money / 100)
deposit = [val_per]
num = int()
profit = money * num
print(val_per)
print(t, s, v, sb)
print("Максимальная сумма, которую вы можете заработать: ", max([t, s, v, sb]))