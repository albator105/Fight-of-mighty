import json
import os
from time import sleep
import sys

path = "data/data.json"


if os.path.exists(path) is not True:
    with open(path, "w") as file:
        file.close()


class Erreurstorage(Exception):
    """
    Class représentant l'absence ou un crash du stockage

    Args:
        Exception (raise): erreur du a aucun stockage
    """

    pass


class Argumentinvalide(Exception):
    """
    Class représentant un argument invalide

    Args:
        Exception (raise): le type de selection donner n'est pas bon
    """

    pass


class Taginnexistant(Exception):
    """
    Class représentant une référence a un Tag qui n'existe pas

    Args:
        Exception (raise): Tag innexistant dans la mémoire
    """

    pass


class Stockagecorrompu(Exception):
    """
    Class représentant la corruption du stockage de données

    Args:
        Exception (raise): données du stockage corrompu
    """

    pass


def obtenir_toute_data(path="data/data.json"):
    """
    fonction qui permet de retourner toutes les données contenues dans la sauvegarde

    Args:
        path (str, optional): le chemin vers le stockage. Defaults a "data/data.json".

    Raises:
        Erreurstorage: problème survenu dans le stockage

    Returns:
        dict: toute les données du json en dictionnaire python
    """
    try:
        with open(path, "r") as file:
            jsonContent = file.read()
            data = json.loads(jsonContent)
            return data
    except:
        raise Erreurstorage("[Storage] un problème est survenu dans le stockage")


def obtenir_data(Tag):
    """
    Fonction permettant d'obtenir une valeur dans le stockage à partir d'un tag

    Args:
        Tag (str): le nom du Tag

    Raises:
        Taginnexistant: le tag demandé n'existe pas
        Erreurstorage: du a un problème d'accès au stockage
        Argumentinvalide: du au tag qui n'est pas un string

    Returns:
        str, bool, int, float : La donnée stocké en valeur
    """
    if isinstance(Tag, str):
        if os.path.exists(path):
            try:
                with open(path, "r") as file:
                    data = json.load(file)
                if Tag in data:
                    return data[Tag]
                else:
                    raise Taginnexistant(
                        "[Storage] le Tag demander n'existe pas dans la mémoire"
                    )
            except:
                raise Erreurstorage(
                    "[Storage] un problème est survenu dans le stockage"
                )
        else:
            raise Erreurstorage("[Storage] le stockage n'existe pas")
    else:
        raise Argumentinvalide("[Storage] le tag doit être obligatoirement un string")


def stocke_data(Tag, valeur):
    """
    Fonction permettant de stocker des données de manière définitive
    si le tag n’existe pas, il est créé automatiquement, si le tag est
    déjà présent alors la valeur en est modifiée.

    Args:
        Tag (str): le tag pour le retrouvé
        valeur (int, float, str; bool): la valeur du Tag

    Raises:
        Erreurstorage: du a un problème d'accès au stockage
        Argumentinvalide: du au tag qui n'est pas un string

    Returns:
        bool: True si tout c'est déroulé comme prévu, False si un problème est survenu
    """
    if isinstance(Tag, str):
        if os.path.exists(path):
            try:
                with open(path, "r") as file:
                    data = json.load(file)

                data[Tag] = valeur
                with open(path, "w") as file:
                    json.dump(data, file)
                return True
            except:
                return False

        else:
            raise Erreurstorage("[Storage] le stockage n'existe pas")
    else:
        raise Argumentinvalide("[Storage] le tag doit être obligatoirement un string")


def reinitialisation_data(path="data/data.json"):
    """
    Fonction permettant la réinitialisation des données total

    Args:
        path (str, optional): le chemin vers le stockage. Defaults a "data/data.json".

    Returns:
        bool: true si l'opération a réussi, false s’il y a échec
    """
    if os.path.exists(path):
        os.remove(path)
    with open(path, "w") as file:
        file.write("{}")
    sleep(0.5)  # temps d'écrasement des données
    try:
        with open(path, "w") as file:
            data = dict()
            data = {
                "name":"Player",
                "niveau": 1,
                "skill_point": 0,
                "experience": 0,
                "next_lvl_up":100,
                "force": 10,
                "vie_max": 100,
                "mana": 100
            }
            json.dump(data, file)
        return True
    except:
        return False


def check_data(path="data/data.json"):
    """
    Fonction permettant de dire si le stockage est corrompu ou si il est valide

    Args:
        path (str, optional): le chemin vers le json. Defaults a "data/data.json".

    Raises:
        Stockagecorrompu: le stockage est corrompu

    Returns:
        bool: true si le stockage est valide et false si il est corrompu
    """
    try:
        with open(path) as file:
            data = json.load(file)
        if isinstance(data["niveau"], int):
            if isinstance(data["skill_point"], int):
                if isinstance(data["experience"], int):
                    if isinstance(data["force"], int):
                        if isinstance(data["vie_max"], int):
                            if isinstance(data["next_lvl_up"], int):
                                if isinstance(data["name"], str):
                                    if isinstance(data["mana"], int):
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        raise Stockagecorrompu("[Storage] le stockage est corrompu !!!")


def chargeurstorage(path="data/data.json"):
  try:
    if check_data():
        pass
    else:
        code = reinitialisation_data()
        if code == False:
            sys.exit()
  except Stockagecorrompu:
    code = reinitialisation_data()
    if code == False:
            sys.exit()