import json
from crew import build_fleet


def save_fleet(fleet, path):
    """Enregistre une flotte"""

    data = fleet.to_dict()
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_fleet(path):
    """Charge la flotte"""

    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        return build_fleet(data)
    except FileNotFoundError:
        raise ValueError(f'aucune sauvegarde « {path} »')
    except json.JSONDecodeError:
        raise ValueError(f'la sauvegarde « {path} » est corrompue')
    except KeyError:
        raise ValueError(f'la sauvegarde « {path} » est incomplète')
    except ValueError as error:
        raise ValueError(str(error))