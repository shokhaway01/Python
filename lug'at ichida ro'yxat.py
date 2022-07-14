dasturchilar = {
    'ali':["HTML", "CSS", "JS"],
    'shoh':["HTML", "CSS", "Python"],
    "vali":["C++", "SQL", "C#"]
    }

for ism, info in dasturchilar.items():
    print(f"\n{ism.title()} - ismli o\'quvchi :")
    for til in info:
        print(f"{til.upper()}", end=" ")


