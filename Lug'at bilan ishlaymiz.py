talaba = {
    "Osmona":"Aziz",
    "Sabiw":"Shahob",
    "Mirjahon":"Visola",
    "Shohjahon":"???",
    "Javlon":"Marjon",
    "Ilhom":"Sarvinoza",
    "Elik":"Dilnoz",
    "Samandar":"Gulxayo"
        }
brazzer = talaba.get("Elyor", "Yuqal sassiq")
for a,b in talaba.items():
    print(f" {a.title()}ning tyolkasi - {b.upper()} ")
print(brazzer)


print("-------------------------------------------")
print("Имена мужей:")
for value in talaba.keys():
    print("   ", value)


cars = {
    "Chevrolet": 1_500_000,
    "Toyota": 2_300_000,
    "Ford": 80_000,
    "Lamborghini": 120_000
    }
listochek = ["Toyota", "Chevrolet", "Nissan", "Ravon"]
print("-------------------------------------------")
for car in cars:
    if car in listochek:
        print(f"{car.title()} стоит ${cars[car]}")
    else:
        print("В нашем автосалоне нет такого авто")

menu_1 = {
    "osh":"50.000",
    "jiz":"12.500",
    "Tuxum-Sasiska":"5.000",
    "Rolton":"1.500.000",
    "Manti":"25.000"
    }

zakaz = ["osh", "jiz", "qovurdoq","manti"]

for food in menu_1:
    if food in zakaz:
        print(f"{food.title()} {menu_1[food]}")
    else:
        print("DNS")








