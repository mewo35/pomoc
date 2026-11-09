import os

script_dir = os.path.dirname(os.path.abspath(__file__))
soubor_cesta = os.path.join(script_dir, "data.txt")
print(f"Otevíram soubor v adresáři: {script_dir}")

try:
    with open(soubor_cesta, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print(f"soubor {soubor_cesta} nebyl nalezen.")