ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


def add_member(crew):
    new_crew = {"last_name": "", "first_name": "", "gender": "", "age": 0, "role": ""}
    m = "M"
    f = "F"
    flag = True
    while True:
        name_in_list = False
        print("Donnez lui un nom :")
        new_crew["last_name"] = str(input())
        for i in crew:
            if i["last_name"].lower() == new_crew["last_name"].lower():
                print("Nom déjà dans la liste")
                name_in_list = True
                break
        if name_in_list:
            continue
        if len(new_crew["last_name"]) < 3 or len(new_crew["last_name"]) > 15:
            continue
        print("Donnez lui un prénom :")
        new_crew["first_name"] = str(input())
        if len(new_crew["first_name"]) < 3 or len(new_crew["first_name"]) > 15:
            continue
        print("Donnez lui un genre")
        new_crew["gender"] = str(input()).upper()
        if new_crew["gender"] not in (m,f):
            print("Genre non valide")
            continue
        print("Donnez lui un âge")
        try:
            new_crew["age"] = int(input())
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide")
            continue
        print(f"liste des rôles : {ROLES}")
        print("Donnez lui un rôle")
        new_crew["role"] = str(input()).lower()
        for i in ROLES:
            if i == new_crew["role"]:
                flag = False
        if flag:
            print("Vous devez choisir un rôle présent dans la liste")
            continue
        crew.append(new_crew)
        print(new_crew)
        break
    return crew

def remove_member(crew):
    while True:
        print("Entrez un nom :")
        last_name = str(input().lower())
        flag = True
        counter = 0
        for i in crew:
            counter = counter + 1
            print(counter)
            if i["last_name"].lower() == last_name:
                flag = False
                counter = counter - 1
                crew.pop(counter)
                print("Membre supprimé")
                print(crew)
                break
        if flag:
            print("Pas de membre ayant ce nom")
            continue
        else :
            return crew
    
    
        



