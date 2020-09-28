import datetime
import os
from pathlib import Path

import chardet
import pandas as panda


class FileReader:
    """
    Cette classe s'occupe de la lecture et la gestion du jeu de donnée.

    On peut y récuperer les informations du fichier
    ainsi que les données du fichier.
    """

    def __init__(self, path):
        """ Constructeur de la classe Filereader

        on passe en paramètre le chemin du fichier
        on initialise les différents attributs à vide
        on définit également l'affichage des données
        on crée un dataframe à partir des données du fichier """

        self.file_path = path
        self.size = ""
        self.encoding = ""
        panda.set_option('display.max_columns', None)
        panda.set_option('display.width', 200)
        self.df = panda.read_csv(self.file_path)
        self.delete_first_column()

    def delete_first_column(self):
        """ Cette fonction permet de supprimer la première colonne d'un fichier

            Cette première colonne correspond aux indexes de chaque donnée, et peut nuire
            aux traitements que l'on y associe par la suite """

        del self.df['Unnamed: 0']

    def display_size_file(self):
        """ Cette fonction permet de retourner la taille en octet du fichier. """

        self.size = str(os.path.getsize(self.file_path))
        return self.size

    def display_encoding_file(self):
        """ Cette fonction permet de retourner l'encodage du fichier.  """

        file = Path(self.file_path)
        self.encoding = str(chardet.detect(file.read_bytes()).get("encoding"))
        return self.encoding

    def display_date_modif_file(self):
        """ Cette fonction permet de retourner la date de modification du fichier. """

        return datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))

    def get_data(self):
        """ Cette fonction permet de retourner le dataframe avec les données du fichier.  """

        return self.df


class FileFormatException(Exception):
    """
    Cette classe permet de gérer l'exception du format de fichier.

    L'objectif de cette classe est de créer une exception, qui serait générée dans le main,
    dans le cas où le type de fichier serait différent du format csv.
    """

    def __init__(self,*args,**kwargs):
        """ Constructeur de la classe FileFormatException """

        Exception.__init__(self,*args,**kwargs)
