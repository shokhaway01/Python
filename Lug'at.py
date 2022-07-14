mevalar = {
        'olma':'Яблоко',
        "banan":"банан",
        "ananas":"ананас",
        "O\'rik":"абрикос"
           }
#print(mevalar["ananas"])
#print(mevalar["banan"])
#print(mevalar["O'rik"])
#print(mevalar["olma"])
#print(mevalar["ananas"])
meva = input("-->")
for a in meva:
    pain = mevalar.get(meva, f"uzin {meva}san")
print(pain)
