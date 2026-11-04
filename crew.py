from fleet import Fleet
from person import Mentalist, Operator
from spaceship import Spaceship


def build_fleet(data):
    """Construit une flotte complète à partir des données fournies."""
    

    fleet = Fleet(data["name"])
    for spaceship_data in data["spaceships"]:
        spaceship = Spaceship(
            spaceship_data["name"],
            spaceship_data["ship_type"],
            spaceship_data["condition"],
        )
        for member_data in spaceship_data["crew"]:

            member_type = member_data["type"]
            common_data = (
                member_data["first_name"],
                member_data["last_name"],
                member_data["gender"],
                member_data["age"],
            )

            if member_type == "operator":
                member = Operator(*common_data, member_data["role"])
                member.experience = member_data.get("experience", 0)
            elif member_type == "mentalist":
                member = Mentalist(*common_data)
                if "mana" in member_data:
                    member.mana = member_data["mana"]
            spaceship.add_member(member)
        fleet.add_spaceship(spaceship)
    return fleet