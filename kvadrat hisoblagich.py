#print("Kvadrat hisobladigan qurilma \n \n")

#savol = "Kvadrat hisoblah ucun son kiriting"
#savol += "\n(Chiqish uchun 'exit' ni kiriting) \n -->"
#qiymat = ' '
#while qiymat != "exit":
 #   qiymat = input(savol)
 #   if qiymat !="exit":
#        print(float(qiymat)**2)



#question = "Введите число:"
#question += "\nЧтобы выйти введите  'exit'...\n---> "  
#value = True

#while value:
#   qiymat = input(question)
#   
#    if qiymat == "exit":
#        value = False
#    else:
#        print(int(qiymat)**2)

question = "Введите число:"
question += "\nЧтобы выйти введите  'exit'...\n---> "  
value = True

while True:
    qiymat = input(question)
    
    if qiymat == "exit":
        break
    else:
        print(int(qiymat)**2)
print("Tugadi, chiqib ketish uchun - Alt+F4")


qiymat = 0
while qiymat < 10:
    qiymat+=1
    if qiymat == 5:
        continue
    else:
        print(qiymat)
