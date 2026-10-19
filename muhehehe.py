input_jmeno = input("Zadej jmeno: ")
input_vlastnost = input("vlastnost: ")
print(f"jmenuji se {input_jmeno} a moje vlastnost je {input_vlastnost}")
#tohle je input procvičování :3

input_uživatel = input("Zadej uživatelské jméno: ")
if input_uživatel == "admin":
    print("...")

input_heslo = input("Zadej heslo: ")
if input_heslo == "nu-uh":
    print("heslo je spravne")

else:
    print("heslo nebo uživatelské jméno je špatné")
#tohle je if a else procvičování :3

teplota = int(input("Zadej teplotu: "))
if teplota < 0:
    print("je zima vezmi si bundu")
elif teplota < 20:
    print("je chladno vezmi si mikinu")
elif teplota < 30:
    print("je teplo vezmi si triko")
else:
    print("je horko vezmi si triko a kraťasy")
#tohle je if, elif a else procvičování :3
