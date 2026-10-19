number_list = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 7,]
unique_numbers = set(number_list)
#vezme všechny čísla a napíše jen jednou
print(f"Unique numbers: {unique_numbers}")
print("puvodni seznam:", number_list)
print(20*"=")

prazdna_mnozina = set()
prazdna_mnozina.add(150)
prazdna_mnozina.add(90)

print("Množina po přidání:", prazdna_mnozina)

if 3 in unique_numbers:
    print("3 je v množině unikatních čísel")
else:
    print("3 není v množině unikatních čísel")