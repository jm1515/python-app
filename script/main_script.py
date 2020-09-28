import argparse

from calcul import Calcul
from file_reader import FileReader
from display import Display
from args_handler import ArgsHandler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("dialog")
    parser.add_argument("log")
    args = parser.parse_args()
    path_arg = args.path.__str__()
    dialog_arg = args.dialog.__str__()
    log_arg = args.log.__str__()

    args_handler = ArgsHandler()

    path_dialog = args_handler.get_path_from_args(path_arg, "Veuillez saisir le bon chemin du fichier : \n")
    dialog = args_handler.check_input_response(dialog_arg, "Souhaitez-vous un dialogue (oui/non) ? \n")
    log = args_handler.check_input_response(log_arg, 'Souhaitez-vous enregistrer les informations (oui/non) ? \n')

    file_reader = FileReader(path_dialog)
    calcul = Calcul(file_reader)
    display = Display()

    if dialog == 'non':
        display.no_dialog(calcul, log, file_reader)

    elif dialog == 'oui':
        display.yes_dialog(calcul, log, file_reader)


if __name__ == '__main__':
    main()
