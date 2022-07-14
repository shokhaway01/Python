names = ["Shokha", "Javlon", "Timur", "Shahob", "Farrux"]

for name in names:
    a = input("Ваше имя пользователя \n-->")
    if a == names:
        print("Добро Пожаловать")
    else:
        print(f"Неправильное имя пользователя {a.title()}. \nПопытайтесь заново")
