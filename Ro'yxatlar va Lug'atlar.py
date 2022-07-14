#ismlar = []
#n=1

#while True:
#    ism = input(f"{n} chi do\'stingizning ismini kiriting:\n-->")
#    n+=1
#    ismlar.append(ism)
#    takrorlash = input("Yana do'slaringiz bormi?\n (Ha/Yoq) \n-->")
#    if takrorlash != "ha":
#        break

#print("Do'stlaringiz ro'yxati: \n")
#for ism in ismlar:
#    print(ism.title(), end = ' , ')


dustlar = {}
ishora = True

while ishora:
    ism = input("Do'stingizni ismi nima?\n -->")
    yosh = input("Do'stingizni yoshi nchada\n-->")
    dustlar[ism] = int(yosh)

    javob = input("Yana ma'lumot kiritishni istaysizmi? (Ha/Yoq)\n -->")
    if javob == "yoq6":
        ishora = False

for ism,yosh in dustlar.items():
    print(f"{ism}, {yosh} yoshda")
