# Задайте список.
#  Напишите программу, которая определит, присутствует 
# ли в заданном списке строк некое число.

# from curses.ascii import isdigit


a = input('Введите список').split()
print(a)
z = False
for i in a:
    if i.isdigit():
        print("Да,присутствует")
        z = True
        break
if z == False:
    print('Нет')
        