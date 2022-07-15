import random

def sontop_user(x = 10):
    tson = random.randint(1,x)
    print(f"Я задумал чилос от 1 до {x}\nМожет отгадаешь?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input("-->")) 
        if taxmin < tson:
            print("Неправильно, задуманное число болше этого!")
        elif taxmin > tson:
            print("Неправильно, задуманное число меньше этого!")
        else:
            break

    print(f"Вы угадли моё число с {taxminlar} раза")
    return taxminlar


def sontop_pc(x = 10):
    input(f"Загадайте число от 1 до {x} и нажмите на Enter . \nЯ отгадаю\n--->")
    minimum = 1
    maximum = x
    taxminlar = 0

    while True:
        taxminlar+=1
        if minimum != maximum:
            taxmin =random.randint(minimum,maximum)
        else:
            taxmin = minimum

        javob = input(f"Вы задумали число {taxmin}?\nЕсли да, напишите(Да)\nЕсли это число меньше чем задуманное напишите(-)\Если больше, то напишите(+)")

        if javob == "-":
            maximum = taxmin - 1
        elif javob == "+":
            minimum = taxmin +1
        else:
            break
    print(f"Ура я отгадал ваше число с {taxminlar} попытки!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_pc = sontop_pc(x)
        taxminlar_user = sontop_user(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


play()
