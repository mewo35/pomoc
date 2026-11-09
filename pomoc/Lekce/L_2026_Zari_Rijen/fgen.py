for i in range(2, 100):
    for x in range(2, i):
        print(f"Kontroluji, jestli je číslo {i} dělitelné číslem {x}.")
        if i % x == 0:
            print(f"{i} není prvočíslo, protože je dělitelné číslem {x}.")
            break
    else:
        print(f"{i} ======= JE PRVOČÍSLO =======")
