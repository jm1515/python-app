import os
from file_reader import FileFormatException


class ArgsHandler:
    """
    Cette classe permet de gérer les arguments saisies.

    L'objectif de cette classe est de vérifier que toutes les saisies sont correctes,
    et si cela n'est pas le cas, on lève des exceptions.
    """

    def get_path_from_args(self, path_arg, input_message):
        """ Cette fonction permet de vérifier le chemin du fichier passé en argument.

            On lève une exception suivant le type de l'erreur """

        error = True
        while error:
            try:
                error = self.check_input_path(path_arg)
            except ValueError:
                print("Problème de saisie, recommencez")
                path_arg = input(input_message)
                error = True
            except FileNotFoundError:
                print("Le fichier n'existe pas")
                path_arg = input(input_message)
                error = True
            except FileFormatException:
                print("Le format du fichier n'est pas le bon")
                path_arg = input(input_message)
                error = True
        return path_arg

    def check_input_path(self, path):
        """ Cette fonction permet de vérifier si le chemin du fichier de données existe

        On lève une exception suivant le type de l'erreur """

        if not path:
            raise ValueError()
        elif not os.path.isfile(path):
            raise FileNotFoundError()
        elif not os.path.splitext(path)[1] == ".csv":
            raise FileFormatException()
        else:
            return False
        return True

    def check_save_file_path(self, path):
        """ Cette fonction permet de vérifier si le chemin pour enregistrer les informations obtenues existe ou pas

        On lève une exception suivant le type de l'erreur """

        if not path:
            raise ValueError()
        elif not os.path.isfile(path):
            raise FileNotFoundError()
        else:
            return False
        return True

    def check_input_response(self, dialog, input_msg):
        """ Cette fonction permet de vérifier si la réponse saisie par l'utilisateur est oui ou non """

        while dialog != "oui" and dialog != "non":
            print("Saisissez oui ou non !")
            dialog = input(input_msg)
        return dialog
