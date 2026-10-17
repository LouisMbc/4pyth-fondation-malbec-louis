from person import Operator, Mentalist

class Spaceship:    
    """Un vaisseau et son équipage"""
    
    def __init__(self, name, ship_type, condition="opérationnel"):
        self.MAX_CREW = 10
        self.name = name
        self.ship_type = ship_type
        self.condition = condition
        self.crew = []
        
    
        
    def add_member(self,member):
        if len(self.crew) >= self.MAX_CREW:
           raise ValueError(f"Le vaisseau est déjà plein")
        elif self.name in self.crew:
            raise ValueError(f"Ce membre est déjà dans le vaisseau")
        else:
            self.crew.append(member)
            
    def find_member(self, name):
        for member in self.crew:
            if member.first_name == name:
                return member
            
    def remove_member(self, name):
        flag = False
        counter = 0
        for member in self.crew:
            counter += 1
            if member.first_name == name:
                counter -= 1
                self.crew.pop(counter)
                flag = True
                return "Membre supprimé"
        if flag == False:
            return None
        
    def check_preparation(self):
        roles = []
        for member in self.crew:
            if isinstance(member, Operator):
                roles.append(member.role)
        if "pilote" in roles and "technicien" in roles:
            return True
        return False

    def watch_round(self):
        for member in self.crew:
            member.act()
            
    def __str__(self):
        counter = 0
        for member in self.crew:
            counter += 1
        return (f"Fearless {self.ship_type} {self.condition} - {counter} membres")
            
                
           
        