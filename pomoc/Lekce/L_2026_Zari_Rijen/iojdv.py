# Funkce pro základní matematické operace.

# Vrátí součet čísel a a b.
def scitani(a, b):
    return a + b

# Vrátí rozdíl čísel a a b.
def odcitani(a, b):
    return a - b

# Vrátí součin čísel a a b.
def nasobeni(a, b):
    return a * b

# Vydělí a číslem b; pokud je b nula, Python vyvolá chybu ZeroDivisionError.
def deleni(a, b):
    return a / b


součet = scitani(5, 3)
print(f"Součet 5 a 3 je 5 + 3 = {součet}")

rozdíl = odcitani(5, 3)
print(f"Rozdíl 5 a 3 je 5 - 3 = {rozdíl}")

součin = nasobeni(5, 3)
print(f"Součin 5 a 3 je 5 * 3 = {součin}")

def deleni(a, b):
    if b == 0:
        raise ValueError("Nelze dělit nulou.")
    return a / b

podíl = deleni(10, 2)
print(f"Podíl 10 a 2 je 10 / 2 = {podíl}")