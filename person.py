ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]
ACTIONS = {
"commandant": "donne ses ordres à l'équipage",
"pilote": "pilote le vaisseau",
"technicien": "répare les moteurs",
"armurier": "vérifie les canons",
"marchand": "négocie une cargaison",
"entretien": "nettoie le vaisseau",
}

class Person:
    """une personne de la flotte"""
    
    def  __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        
    def introduce_yourself(self):
        if self.gender == "M":
            gender = " un homme"
        else:
            gender = " une femme"
        space = " " if len(self.last_name) > 0 else ""
        return f"Je m'appelle {self.first_name}{space}{self.last_name}, je suis {gender} de {self.age} ans  "
 
    def __str__(self):
        return f"{self.first_name}{self.last_name} ({self.gender}, {self.age} ans)"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def remove_member(self, first_name, last_name):
        while True:
            print("Entrez un nom ou un prénom  :")
            last_name = str(input().lower())
            flag = True
            counter = 0
            for i in self.crew:
                counter = counter + 1
                print(counter)
                if i["last_name"].lower() == last_name:
                    flag = False
                    counter = counter - 1
                    self.crew.pop(counter)
                    print("Membre supprimé")
                    print(self.crew)
                    break
                if i["first_name"].lower() == first_name:
                    flag = False
                    counter = counter - 1
                    self.crew.pop(counter)
                    print("Membre supprimé")
                    print(self.crew)
                    break       
            if flag:
                print("Pas de membre ayant ce nom")
                continue
            
class Operator(Person):
    """Un membre d'équipage avec un rôle"""
    
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self.experience= 0
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        if value not in ROLES:
            raise ValueError(f"Rôle inconnu : {value}")
        self._role = value
        
    def act(self):
        print(f"{ACTIONS[self.role]}")
        self.gain_experience()

    def gain_experience(self):  
        self.experience += 1

    def __str__(self):
        introduce = super().__str__()
        return f"{introduce} - {self.role}"

class Mentalist(Person):
    """Un membre de la Seconde Fondation"""
    
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.mana = 5
        
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        self._mana = max(0, min(value, 100))
        
    def act(self):
        self.mana += 10
        return f"{self.first_name} se concentre"
    
    def recharge_mana(self):
        self.mana += 50
        
    def influence(self, operator):
        if self.mana >= 20:
            self.mana -= 20
            operator.act()
        else:
            print(f"{self.first_name} n'a pas assez de mana pour influencer {operator.name}")
            return False

    def __str__(self):
        introduce = super().__str__()
        return f"{introduce} - mentaliste, {self.mana} mana"
    
    
        
                

