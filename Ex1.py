# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#  Элементы нужно выводить в том порядке, в котором они встречаются в списке.
import random


# a = [random.randint(-1000,100000) for i in range(10)]
# print (a)
# for i in a:
#     if a.count(i)==1:
#         print (i,end=" ")

a = [random.randint(-10,10) for i in range(10)]
print (a)
mass = []
for i in a:
    if a.count(i)==1:
        mass.append(i)
print ()
print (mass)