from person import *
from spaceship import *

# crew = [
# {"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
# {"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
# {"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
# {"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
# {"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
# ]

user = Person("Bel", "Riose", "M", 48)
user1 = Person("Fallom", "", "M", 48)
user2 = Operator("Hugo", "Crast", "M", 37, "pilote")
user3 = Mentalist("Joie", "", "F", 25)
user4 = Operator("Louis", "", "F", 25, "technicien")
ship = Spaceship("bato", "baston", "operationnel")
print(user.introduce_yourself())
print(user.__str__())
print(user1.introduce_yourself())
print(user.__str__())
print(user2.__str__())

print(user3.act())
print(user3.influence(user2))
print(user3.__str__())
# print(user.remove_member)

print(ship.add_member(user))
print(ship.add_member(user4))
print(ship.add_member(user2))
print(ship.find_member("Bel"))
print(ship.find_member("Louis"))
print(ship.find_member("Hugo"))
print(ship.remove_member("Bel"))
print(ship.find_member("Bel"))
print(ship.find_member("Louis"))
print(ship.find_member("Hugo"))
print(ship.remove_member("Bel"))
print(ship.check_preparation())
print(ship.watch_round())
print(ship.__str__())
