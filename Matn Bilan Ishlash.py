ism = "Anvar"
country = "Uzbekistan"
city = "Djizzakh"

print("My name is -" + ism)


# F стринг
ism_sharif = f"{ism} - {country}"

print(ism_sharif)

# Пример F стринга

name = "James"
surname = "Bond"

bio = f"Hello, my name is {name} {surname}. I'm from{country}"
print(bio)

print("----------------------------------------------")

onion = "Hello \tWorld"
print(onion.upper())
print(onion.lower())
print(onion.title())
print(onion.capitalize())
# \t оставляет большое пространство между словами в коде


# новые методы

fruit = "   Shalooom    "
print(fruit.lstrip())
print(fruit.rstrip())
print(fruit.strip())



