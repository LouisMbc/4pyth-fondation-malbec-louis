def add_member(crew):
    new_crew = {"last_name":"", "first_name":"","gender":"","age": 0, "role":""}
    while True:
        print("Donnez lui un nom :")
        new_crew["last_name"] = str(input())
        for i in crew:
            if i["last_name"] == new_crew["last_name"]:
            # if crew[i]["last_name"] == new_crew["last_name"]:
                print("Nom déjà dans la liste")
            continue
        if len(new_crew["last_name"]) < 3 or len(new_crew["last_name"]) > 15:
            continue
        print("Donnez lui un prénom :")
        new_crew["first_name"] = str(input())
        if len(new_crew["first_name"]) < 3 or len(new_crew["first_name"]) > 15:
            continue
        print("Donnez lui un genre")
        new_crew["gender"] = str(input())
        print("Donnez lui un âge")
        new_crew["age"] = int(input())
        print("Donnez lui un rôle")
        new_crew["role"] = str(input())
        crew.append(new_crew)
        print(new_crew)
        break
    return crew

