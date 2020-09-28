import sys
import os

from args_handler import ArgsHandler


class Display:
    """
    Cette classe permet de gérer les affichages, ainsi que la sauvegarde du fichier de log.

    L'objectif de cette classe est de s'assurer que les affichages pour un utilisateur soient complets.
    """

    def show_file_reader_info(self, file_reader, display):
        """ Cette fonction permet d'afficher les informations du fichier """

        if display == "oui":
            print("Filesize : " + file_reader.display_size_file() + " octets")
            print("Encoding : " + file_reader.display_encoding_file())
            print("Modifié le :", file_reader.display_date_modif_file())
            print(file_reader.get_data())
        else:
            print("Vous n'avez pas souhaité afficher les informations du fichier \n")

    def show_calcul_info(self, calcul):
        """ Cette fonction permet d'afficher les informations concernant les données
            du fichier """

        print("Nombre de variables : ", calcul.get_nb_var())
        print("Nombre d'observations : ", calcul.get_nb_observation())
        print("Nombre des variables quantitatives : ", calcul.get_nb_var_quantitative())
        print("Nombre des variables qualitatives: ", calcul.get_nb_var_qualitative())
        print("Nom des variables quantitatives : ", calcul.get_var_quantitative())
        print("Nom des variables qualitatives : ", calcul.get_var_qualitative())
        print("\n")

    def show_calcul_info_var_qualitative(self, calcul, display):
        """ Cette fonction permet d'afficher les informations des variables qualitatives
            du fichier """

        calcul.plot_var_qualitative()
        if display == "oui":
            print("------ Informations variables qualitatives : ---------\n")
            print(calcul.get_info_var_qualitative())
        else:
            print("Vous n'avez pas souhaité afficher les informations concernant les variables qualitatives \n")

    def show_calcul_info_var_quantitative(self, calcul, display):
        """ Cette fonction permet d'afficher les informations des variables quantitatives
            du fichier """

        calcul.plot_var_quantitative()
        if display == "oui":
            print("------ Informations variables quantitatives : ---------\n")
            print(calcul.get_info_var_quantitative())
        else:
            print("Vous n'avez pas souhaité afficher les informations concernant les variables quantitatives \n")

    def show_file_info(self, calcul, display, file_reader):
        """ Cette fonction permet d'afficher toutes les informations obtenues
            sur le fichier """

        self.show_file_reader_info(file_reader, display)
        self.show_calcul_info(calcul)
        self.show_calcul_info_var_qualitative(calcul, display)
        self.show_calcul_info_var_quantitative(calcul, display)

    def save_output_on_file(self, calcul, display, path, file_reader):
        """ Cette fonction permet d'enregistrer toutes les informations concernant le fichier,
            ainsi que les données """

        sys.stdout = open(path, "w")
        self.show_file_info(calcul, display, file_reader)
        sys.stdout.close()

    def yes_dialog(self, calcul, fileLog, file_reader):
        """ Cette fonction prend en compte la demande de dialogue par l'utilisateur

        Pour chaque réponse, on vérifie si celle-ci a bien a été saisie
        A la fin, si l'utilisateur souhaite enregistrer les informations obtenues,
        on lui demande le chemin de sauvegarde du fichier, et on s'assure que celui-ci existe """

        check_input = ArgsHandler()

        display = input("Voulez-vous afficher les informations concernant le fichier (oui/non) ?\n")
        display = check_input.check_input_response(display,
                                       "Voulez-vous afficher les informations concernant le fichier (oui/non) ?\n")
        self.show_file_reader_info(file_reader, display)
        self.show_calcul_info(calcul)
        display = input("Voulez-vous afficher les informations concernant les variables qualitatives (oui/non) ?\n")
        display = check_input.check_input_response(display,
                                       "Voulez-vous afficher les informations concernant les variables qualitatives (oui/non) ?\n")
        self.show_calcul_info_var_qualitative(calcul, display)
        display = input("Voulez-vous afficher les informations concernant les variables quantitatives (oui/non) ?\n")
        display = check_input.check_input_response(display,
                                       "Voulez-vous afficher les informations concernant les variables quantitatives (oui/non) ?\n")
        self.show_calcul_info_var_quantitative(calcul, display)
        path = ''

        if fileLog == 'oui':
            display = 'oui'

            error = True
            while error:
                try:
                    path = input("Saisissez le chemin du fichier : \n")
                    if not os.path.isdir(path.strip()):
                        raise ValueError
                    else:
                        error = False
                except ValueError:
                    print("Problème de saisie, recommencez")
                    error = True
                except FileNotFoundError:
                    print("Le fichier n'existe pas")
                    error = True
            print("Les données ont été bien enregistrées \n")
            self.save_output_on_file(calcul, display, path + "/log.txt", file_reader)
        else:
            print("Vous n'avez pas souhaité enregistrer les données \n")

    def no_dialog(self, calcul, fileLog, file_reader):
        """ Cette fonction concerne le cas où aucun dialogue utilisateur n'a été demandé

        Si l'utilisateur a souhaité enregistrer les informations obtenues, dans ce cas-là
        on ne les affiche pas dans le terminal
        La valeur de la variable display sert dans les deux cas, que ce soit pour enregistrer
        (puisque l'on enregistre tout les print dans le fichier de log) ou pour afficher """

        display = 'oui'
        if fileLog == 'oui':
            print("Les données ont été bien enregistrées \n")
            path = os.getcwd() + "/log.txt"
            self.save_output_on_file(calcul, display, path, file_reader)
        else:
            self.show_file_info(calcul, display, file_reader)
            print("Vous n'avez pas souhaité enregistrer les données \n")
