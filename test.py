def ish(ism):
  while ism:
    for ismcha in ism:
      a = ismcha.title()
      savol1 = int(input(f"Salom,{ismcha}. Yoshingiz nechada?\n-->"))


    if savol1 < 18:
      print("Siz Hali yoshsiz !!!")
      break
    savol2 = input("Bizning Shartlar bilan rozimisiz?")
    if (savol2 == "Ha") or (savol2 == "ha"):
      print("Uhladiz")
      sonlar = (range(101))
      for son in sonlar:
        print(f"{son}%")
      "Buzish amalga oshirildi"
    else:
      break
    