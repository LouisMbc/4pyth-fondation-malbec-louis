from person import Operator, Mentalist
from spaceship import Spaceship

class Fleet:
    """la flotte"""
    
    def __init__(self, name):
        self.name = name
        self.spaceships = []
        self.MAX_SPACESHIPS = 15
        
    def add_spaceship(self, spaceship):
        if len(self.spaceships) >= self.MAX_SPACESHIPS:
            raise ValueError(f"La flotte est déjà pleine")
        elif self.name in self.spaceships:
            raise ValueError(f"Ce vaisseau est déjà dans la flotte")
        else:
            self.spaceships.append(spaceship)
            
    def find_spaceship(self, name):
        for spaceship in self.spaceships:
            if spaceship.name.lower() == name.lower():
                return spaceship
            
    def statistics(self):
        roles = []
        counter = 0
        experiences = 0
        nb_ready_ships = 0
        pilote = technicien = armurier = commandant = marchand = entretien = 0
        for spaceship in self.spaceships:
            spaceship_temp = spaceship
            if spaceship_temp.check_preparation():
                nb_ready_ships += 1
            for member in spaceship_temp.crew:
                if isinstance(member, Operator):
                    roles.append(member.role)
                    experiences = experiences + member.experience
                if isinstance(member, Mentalist):
                    counter += 1
        for i in roles:
            match i:
                case "pilote":
                    pilote += 1
                case "technicien":
                    technicien += 1                
                case "armurier":
                    armurier += 1
                case "commandant":
                    commandant += 1
                case "marchand":
                    marchand += 1
                case "entretien":
                    entretien += 1     
        return f"""         Statistiques
                {len(self.spaceships)} Vaisseaux
                {sum(len(s.crew) for s in self.spaceships)} Membres
                {pilote} pilotes
                {technicien} techniciens
                {armurier} armuriers
                {commandant} commandants
                {marchand} marchands
                {entretien} entretiens
                {counter} Mentalistes
                {experiences/len(roles)} d'experience en moyenne pour les opérateurs
                {nb_ready_ships} Vaisseaux prêts
                
    """
