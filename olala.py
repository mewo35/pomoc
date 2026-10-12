squares = [x**2 for x in range(10)]
print(f"squares numbers from 0 to 9: {squares}")

mocnina = []
for x in range(10):
    mocnina.append(x**2)
    print(x, x**2)

words = ["python", "is", "awesome"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")