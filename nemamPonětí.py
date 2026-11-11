classmates= ["Ondřej Bojko", "Jakub Fojcik", "Barbora Gašová", "Samuel Gomola", "Matěj Helt", "Tobiáš Kluz", "Adam Marek", "Petr Michalik", "Michal Mrugala", "Patrik Pohl", "Adam Prokop", "Jonáš Rajca", "Jakub Sikora", "Vít Sikora", "Šimon Šimko", "Samuel Szcerba", "Václav Szurman", "Adam Topiarz", "David Vavrys", "Dominik Wybranietz"]
classmate_numbers = {classmate: i + 1 for i, classmate in enumerate(classmates)}

print("classmates: ")
for classmates in classmates:
    print(classmates)

input_classmate = input("Enter a classmate's name to get their number: ")
if input_classmate in classmate_numbers:
    print(f"{input_classmate}'s number is: {classmate_numbers[input_classmate]}")

print("====================")

print("please input a number between 1 and 20")
input_number = input("Enter a classmate's number to get their name: ")
if input_number in classmate:
    print(f"The classmate with number {input_number} is: {classmate[input_number]}")


#zítra se na to podívám, už chci spinkat :)