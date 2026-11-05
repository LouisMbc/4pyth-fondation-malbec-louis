from crew import build_fleet
from fleet_data import FLEET_DATA
from person import Mentalist, Operator, ROLES
from spaceship import Spaceship
from storage import load_fleet, save_fleet


def ask_ship(fleet):
    name = input("Nom du vaisseau : ").strip()
    spaceship = fleet.find_spaceship(name)
    if spaceship is None:
        raise ValueError(f"Vaisseau inconnu : {name}")
    return spaceship


def ask_person_data():
    first_name = input("Prénom : ").strip()
    last_name = input("Nom : ").strip()
    gender = input("Genre (M/F) : ").strip().upper()
    age = int(input("Âge : "))
    return first_name, last_name, gender, age


def add_member(fleet):
    spaceship = ask_ship(fleet)
    member_type = input("Type de membre (operateur/mentaliste) : ").strip().lower()
    person_data = ask_person_data()
    if member_type in ("operateur", "operator"):
        role = input(f"Rôle ({', '.join(ROLES)}) : ").strip().lower()
        member = Operator(*person_data, role)
    elif member_type == "mentaliste":
        member = Mentalist(*person_data)
    else:
        raise ValueError(f"Type de membre inconnu : {member_type}")
    spaceship.add_member(member)
    print("Membre ajouté.")


def remove_member(fleet):
    spaceship = ask_ship(fleet)
    name = input("Prénom du membre à retirer : ").strip()
    if spaceship.find_member(name) is None:
        raise ValueError(f"Membre inconnu : {name}")
    spaceship.remove_member(name)
    print("Membre supprimé.")


def display_fleet(fleet):
    for spaceship in fleet.spaceships:
        print(f"{spaceship.name} ({spaceship.ship_type}, {spaceship.condition})")
        if spaceship.crew:
            for member in spaceship.crew:
                print(f"  - {member}")
        else:
            print("  - Aucun membre")


def check_spaceship(fleet):
    spaceship = ask_ship(fleet)
    if spaceship.check_preparation():
        print(f"{spaceship.name} est prêt.")
    else:
        print(f"{spaceship.name} n'est pas prêt.")


def add_spaceship(fleet):
    name = input("Nom du vaisseau : ").strip()
    ship_type = input("Type du vaisseau : ").strip()
    condition = input("État (opérationnel/endommagé) : ").strip()
    fleet.add_spaceship(Spaceship(name, ship_type, condition))
    print("Vaisseau ajouté.")
    

def ask_save(fleet):
    path = input("Nom du fichier de sauvegarde: ").lower().strip()
    save_fleet(fleet, path)
    print(f"Flotte Galactica sauvegardée dans {path}.")
    

def ask_load(fleet):
    path = input("Fichier à charger [fleet.json] : ").strip() or "fleet.json"
    try:
        loaded_fleet = load_fleet(path)
    except ValueError as error:
        print(f"Chargement impossible : {error}")
        return fleet
    print(f"Flotte {loaded_fleet.name} chargée depuis « {path} ».")
    return loaded_fleet
    

def main():
    fleet = build_fleet(FLEET_DATA)
    while True:
        print(
            "\n===== Flotte marchande – Poste de commandement =====\n"
            "[1] Ajouter un membre\n"
            "[2] Retirer un membre\n"
            "[3] Afficher la flotte\n"
            "[4] Vérifier un vaisseau\n"
            "[5] Ajouter un vaisseau\n"
            "[6] Statistiques de la flotte\n"
            "[7] Sauvegarder la flotte\n"
            "[8] Charger une flotte\n"
            "[0] Quitter"
        )
        try:
            choice = int(input("Votre choix : "))
            if choice == 1:
                add_member(fleet)
            elif choice == 2:
                remove_member(fleet)
            elif choice == 3:
                display_fleet(fleet)
            elif choice == 4:
                check_spaceship(fleet)
            elif choice == 5:
                add_spaceship(fleet)
            elif choice == 6:
                print(fleet.statistics())
            elif choice == 7:
                ask_save(fleet)
            elif choice == 8:
                fleet = ask_load(fleet)
            elif choice == 0:
                break
            else:
                print("Commande inconnue.")
        except ValueError as error:
            print(f"Erreur : {error}")
    return fleet


if __name__ == "__main__":
    main()