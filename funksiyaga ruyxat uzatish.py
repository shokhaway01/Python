def bahola(ismlar):
  baholar = {}
  while ismlar:
    ism = ismlar.pop()
    baho = int(input(f"Talaba {ism.title()}ning bahosini kiriting\n--->")) 
    baholar[ism] = int(baho)
    savol = input("baholanganlar ro'yxatini chiqarilishini hohllaysizmi?(xa/yoq)\n--->")
    if (savol != "ha") and (savol != "Ha"):
      continue
    else:
      print(baholar)
ismlar = ["ali","vali","shoh","tima"]
ismlar.reverse()

bahola(ismlar)