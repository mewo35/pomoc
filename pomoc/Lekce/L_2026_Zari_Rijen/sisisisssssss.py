#slovnik idk
contacts = {
    "name": "Nela",
    "surname": "Dekanikova",
    "age": 666,
    "hobby": "badminton",
    "city": "Ostava",
    "mail": "nela.dekanikova@example.com",
    "phone": "+420 123 456 789",
    "country": "Czech Republic"
}
print(f"Jmenuji se {contacts['name']} {contacts['surname']}, je mi {contacts['age']} let a moje zaliba je {contacts['hobby']}.")
#vytiskne celou strukturu slovniku

print(f"Name: {contacts['name']}")
#vytiskne jenom jmeno ze slovniku

contacts["age"] = 667
#zmeni hodnotu veku ve slovniku
print(f"Age: {contacts['age']}")

contacts["city"] = "Ostava"
#prida do slovniku novou hodnotu mesto
print(contacts)

phone_number = contacts.get("phone")
#ziska hodnotu telefonniho cisla ze slovniku
print(f"Phone number: {phone_number}")