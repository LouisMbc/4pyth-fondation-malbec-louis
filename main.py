from crew import *

crew = [
    {"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
    {"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
    {"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
    {"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
    {"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
]

def menu():
    print("""
                ===== Flotte marchande – Gestion de l'équipage =====
                            [1] Ajouter un membre
                            [2] Retirer un membre
                            [3] Afficher l'équipage
                            [4] Vérifier l'équipage
                            [0] Quitter
    """)
    print("votre choix : ")
    choix = int(input())
    match choix:
        case 1:
            add_member(crew)
        case 2:
            remove_member(crew)
        case 3:
            print("")
        case 4:
            print("")
        case 0:
            print("")
        case _:
            print("Commande inconnue")

while True:
    menu()
print(crew)