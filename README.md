# Flotte marchande

Application Python en ligne de commande permettant de gérer une flotte de
vaisseaux et leurs équipages.

## Lancer le programme

Depuis le dossier du projet :

```bash
python3 main.py
```

Le programme démarre avec la flotte `Galactica` définie dans
`fleet_data.py`.

## Menu

| Choix | Fonction |
| --- | --- |
| **1** | Ajouter un membre à l'équipage d'un vaisseau. Le programme demande le vaisseau, le type de membre, son identité et son rôle éventuel. |
| **2** | Retirer un membre d'un vaisseau à partir de son prénom. |
| **3** | Afficher les vaisseaux, leur état et les membres de chaque équipage. |
| **4** | Vérifier si un vaisseau est prêt. Il doit notamment avoir un pilote et un technicien. |
| **5** | Ajouter un vaisseau à la flotte. |
| **6** | Afficher les statistiques : effectifs par rôle, mentalistes, expérience moyenne, vaisseaux endommagés et vaisseaux prêts. |
| **7** | Sauvegarder la flotte courante dans un fichier JSON. |
| **8** | Charger une flotte depuis un fichier JSON. En cas d'erreur, la flotte courante est conservée. |
| **0** | Quitter le programme. |

Les fichiers JSON sont lisibles et modifiables avec un éditeur de texte.
Toutefois, le chargement valide leur structure : un rôle inconnu, une donnée
manquante ou un fichier JSON corrompu est refusé. La valeur du mana est bornée
par son setter à 100.



## Déclaration d'usage de l'IA

J'ai utilisé l'ia pour coderà ma place certaine partie de fonction que je n'arrivais pas à coder moi-même.
Aussi pour corriger certaines erreurs qu'il a fallut régler dans certaine des classes lorsque j'ai implémenté le menu.
Enfin je l'ai aussi utilisé pour générer ce présent fichier.
