number = int(input("Zadejte číslo: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

age = int(input("Zadejte svůj věk: "))
if age >= 16 and age < 18:
    print("Jste mladistvý.")
else:
    print("Jste dospělý.")

number = 10

if number % 2 == 0:
    print("number is even")
else:
    print("Number is odd")
# % je MODULO, vrací zbytek po dělení

print(7 % 2)


nakupní_kosik = []

if nakupní_kosik:
    print("Je v něm něco nelegalního")
else:
    print("Člověk je chudý")

povolene_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "jablko"

if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolené ovoce.")
else:
    print(f"{moje_ovoce.capitalize()} není povolené ovoc.")
#capitalize dělá počatečční písmeno velké