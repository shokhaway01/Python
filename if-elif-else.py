menu = ["Chucvara", "Lavash", "Manti", "Spagetti", "XotDog"]
ovqat = input("Какую еду хотите заказать? \n-->").title()
ovqat.title()


if ovqat in menu:
    print("Ваша заявка принята")
elif ovqat == "Nima zakaz qilay":
    print(f"Bizda {menu} - nomli ovqatlar bor")
else:
    print("Uzur bunaqa ovqat yo\'q")
