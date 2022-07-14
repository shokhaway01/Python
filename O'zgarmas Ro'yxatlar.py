cars = ["Chevrolet", "Ford", "Audi", "BWM", "Mustang", "lamborghini", "Bugatti"]
cars.sort()
print(cars)

#cars.sort(reverse=True)
#print(cars)

#print(sorted(cars))
#print(sorted(cars, reverse=True))




#num = [55, 66, 77, 88, 99, 110, 75, 11, 22 , 75, 150]
#print(num)
#num.reverse()
#print(num)
#print(len(num))

#num.append(555)
#print(num)
#print(len(num))


#spisok = list(range(0,180,2))
#print(max(spisok))
#print(min(spisok))
#print(sum(spisok))
#print("---------------------------------------------")
#print(spisok[25:50])



print("------------------------------------------")
my_cars = cars[:]
my_cars.remove("Chevrolet")
my_cars.insert(0, "Volvo")
del my_cars[2]
del my_cars[:3]
print(my_cars)

toys = ("toy", "moy", "loy", "hoy")
print(toys)

toys = list(toys)
toys.append("guys")
print(toys)
