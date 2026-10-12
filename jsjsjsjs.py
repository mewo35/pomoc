tuple = (1,2,3,4,5)
print(f"Tuple: {tuple}")
try:
    tuple[0] = 10
except TypeError as e:
    print(f"Chyba: {e}")
