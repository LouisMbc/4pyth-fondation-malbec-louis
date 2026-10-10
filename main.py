from person import *

crew = [
{"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
{"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
{"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
{"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
{"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
]

user = Person("Bel", "Riose", "M", 48)
user1 = Person("Fallom", "", "M", 48)
user2 = Operator("Hugo", "Crast", "M", 37, "pilote")
user3 = Mentalist("Joie", "", "F", 25)
print(user.introduce_yourself())
print(user.__str__())
print(user1.introduce_yourself())
print(user.__str__())
print(user2.__str__())

print(user3.act())
print(user3.influence(user2))
print(user.remove_member)

