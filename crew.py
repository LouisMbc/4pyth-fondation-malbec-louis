from fleet import Fleet
from person import Mentalist, Operator
from spaceship import Spaceship


def build_fleet(data):
    """Construit une flotte complète à partir des données fournies."""
    
    # On crée d'abord l'objet Fleet principal. C'est lui qui va contenir
    # tous les vaisseaux de la flotte.
    fleet = Fleet(data["name"])

    # La clé "spaceships" contient une liste de dictionnaires.
    # On parcourt cette liste pour créer chaque vaisseau un par un.
    for spaceship_data in data["spaceships"]:
        # On récupère les informations du vaisseau dans le dictionnaire.
        # Le constructeur de Spaceship a besoin de son nom, de son type
        # et de son état (opérationnel ou endommagé).
        spaceship = Spaceship(
            spaceship_data["name"],
            spaceship_data["ship_type"],
            spaceship_data["condition"],
        )

        # Chaque vaisseau possède une clé "crew" qui contient la liste
        # des membres de son équipage.
        for member_data in spaceship_data["crew"]:
            # Le type permet de savoir quelle classe Python instancier :
            # un opérateur devient un objet Operator et un mentaliste
            # devient un objet Mentalist.
            member_type = member_data["type"]

            # Ces quatre informations sont communes aux deux classes.
            # On les regroupe dans un tuple pour éviter de répéter
            # le même code dans les deux branches du if.
            common_data = (
                member_data["first_name"],
                member_data["last_name"],
                member_data["gender"],
                member_data["age"],
            )

            if member_type == "operator":
                # Un opérateur possède une information supplémentaire :
                # son rôle, par exemple "pilote" ou "technicien".
                # L'étoile (*) décompose le tuple common_data en plusieurs
                # arguments avant d'ajouter le rôle à la fin.
                member = Operator(*common_data, member_data["role"])
            elif member_type == "mentalist":
                # Un mentaliste n'a pas de rôle. Il est donc créé seulement
                # avec les informations communes à tous les membres.
                member = Mentalist(*common_data)

                # La classe Mentalist commence normalement avec 100 points
                # de mana. On applique quand même la valeur présente dans
                # les données pour reconstruire exactement l'état indiqué.
                if "mana" in member_data:
                    member.mana = member_data["mana"]
            
            # Le membre maintenant créé est ajouté à son vaisseau.
            # On utilise la méthode de Spaceship afin de conserver ses
            # règles (par exemple la limite de 10 membres).
            spaceship.add_member(member)

        # Une fois tous les membres ajoutés, on ajoute le vaisseau terminé
        # à la flotte. La méthode Fleet vérifie notamment sa capacité.
        fleet.add_spaceship(spaceship)

    # On retourne la flotte complète pour que le code appelant puisse
    # l'utiliser, par exemple pour rechercher un vaisseau ou afficher
    # ses statistiques.
    return fleet