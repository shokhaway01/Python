car0 = {
        'model':"gentra",
        'rangi':"qora",
        'yili':2019,
        "narh":15000,
        'km':20000
    }
car1 = {
        'model':"nexia",
        'rangi':"qizil",
        'yili':2012,
        "narh":3500,
        'km':180000
    }
car2 = {
        'model':"BMW",
        'rangi':"Dark-Blue",
        'yili':2022,
        "narh":37000,
        'km':0
    }

car = car2
print(f"{car['model'].title()}\n"
      f"{car['rangi'].title()}\n"
      f"{car['yili']}\n"
      f"{car['km']}"
      )

cars = [car0, car1, car2]
cars[0]['rangi']= "ko'k"
for car in cars:
    print(car)
    print("\n\n")
