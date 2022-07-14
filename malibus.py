malibus = []
for n in range(15):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)

for malibu in malibus[:5]:
    malibu["rang"] = "qizil"

for malibu in malibus[5:8]:
    malibu["rang"] = "qora"

for malibu in malibus[8:16]:
    malibu["rang"] = "oq"

#-----------------------------------------------

for malibu in malibus[0:8]:
    malibu['korobka'] = "mehanika"

for malibu in malibus[8:15]:
    malibu['korobka'] = "avto"


for malibu in malibus:
    if malibu["korobka"] == "avto":
        malibu["narh"] = 40000
    else:
        malibu["narh"] = 35000
for malibu in malibus:
    print(malibu)

