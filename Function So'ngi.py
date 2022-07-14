from math import sqrt
import random as r

# lambda argument:ifoda
# lambda argument, argument2, argument3:ifoda

# uzunlik = lambda x,y,z: (x*y)**z
# print(uzunlik(2,10,2))
# print(uzunlik(5,8,1))

# def daraja(n):
#   return lambda x: x**n

# kvadrat = daraja(5)
# print(kvadrat(4))

# kub = daraja(5)
# print(kub(4))

# sonlar = list(range(1,11,2))
# # ildizlar = (list(map(sqrt,sonlar))) # - map: uzgaruvchi ichidagi har bir qiymatga qullaydi
# # print(ildizlar)

# kvadratlar = list(map(lambda x: x**2 , sonlar))
# for kvadrat in kvadratlar:
#   print(kvadrat)

# a = [1,2,3,4,5,6]
# b = [6,5,4,3,2,1]

# summa = list(map(lambda x,y: x+y,a,b))

# print(summa)

ism = ["Aziz","Shoh","Saman","Jaxa","Shahob","Dosya","Mirjahon","Elik","Elyor","Olim","Jakoy","Sancho"]

sonlar = r.sample(ism,2)
print(f"Kimlar Do'st Ekan, Faqat bir martta ishlatilsin!!!\n--->{sonlar}")