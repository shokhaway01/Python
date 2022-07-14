# Листс или же список

friends = ["Anvar", "Shayxislom", "Temur", "Shohjaxon"]

#print(friends[0])
#print(friends[1])
#print(friends[2])
#print(friends[3])
print(friends)
friends[3] = "Javlon"
#print(friends[3])
print(friends)

#Чтобы добавить в список элемент мы используем метод (append)

friends.append("Shahobiddin")
print(friends)

friends.insert(0, "Dosya")
print(friends)

friends.insert(5,"Shoma")
print(friends)

cars = []
cars.append("Nexia 3")
cars.append("Damas")
cars.append("Cobalt")
cars.append("Malibu")
print(cars)
del cars[1]
print(cars)

print("---------------------------------------------")

bozorlik = []

bozorlik.append("Sovun")
bozorlik.append("Poroshok")
bozorlik.append("Tish Pastasi")
bozorlik.append("Oyoq kremi")
print(bozorlik)

olingan = bozorlik.pop(1)
print(olingan)
print(bozorlik)

olingan = bozorlik.pop()
print(olingan)
print(bozorlik)


