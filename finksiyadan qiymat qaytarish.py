def tuliq_ism(ism = "Shokha", familiya = "Way"):
    name = (f"{ism} {familiya}")
    return name

tuliq_ism()

talaba1 = tuliq_ism("Magister", "Yoda")
talaba2 = tuliq_ism("Kvaygon", "Jin")
talaba3 = tuliq_ism("Obi-Van", "Kenobi")
talaba4 = tuliq_ism("Dart", "Vader")

print(f"{talaba1},\n{talaba2},\n{talaba3}, \ndarsga kech qodi")


def avto_info(kompaniya = "" ,model = "",narh = None,korobka = "",rangi = "",yili = None):
    """Moshinalar haqida ma'lumot beradigon qurilma"""
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'narh':narh,
        'korobka':korobka,
        'rangi':rangi,
        'yili':yili
        }
    return avto

avto1 = avto_info("NISSAN", "R34", None,"avtomat","qizil",2022)
avto2 = avto_info("TOYOTA", "Supra", None,"mexanika","oq",2019)

avtolar = [avto1, avto2]
for avto in avtolar:
    if avto["korobka"] == "avtomat":
        avto["narh"] = 35000
    elif avto["korobka"] == "mexanika":
        avto["narh"] = 25000
    else:
        avto["narh"] = None
    print(avto, end ="\n\n")

