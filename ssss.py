python_devs=["Nela", "Petr", "Jirka", "Marek", "Jana", "Lucie", "Karel", "Eva", "Tomas", "Veronika"]
java_devs=["Hana", "Miroslav", "Pavla", "Ondrej", "Martina", "Lukas", "Petra", "David", "Jana", "Michal"]

#nebo

vsechny_devs = set(python_devs) | set(java_devs)
print("Všichni vývojáři (sjednocení):", vsechny_devs)
print(20*"=")

#operace pruniku (A ∩ B)
polyglot_devs = set(python_devs) & set(java_devs)
print("Vyvojáři, kteří ovládají Python i Java (průnik):", polyglot_devs)
#& spojuje jen ty, kteří jsou v obou množinách, ,polyglots vybíra z toho předchozího seznamu jen ty, kteří jsou v obou množinách

#rozdíl množin (A - B)
python_only_devs = set(python_devs) - set(java_devs)
print("Vývojáři, kteří ovládají pouze Python (rozdíl):", python_only_devs)
print(20*"=")
#to stejne akorat změna znamenka