import os

from script.calcul import Calcul
from script.file_reader import FileReader

PATH = os.getcwd() + "/data/iris.csv"


def init():
    file_reader = FileReader(PATH)
    calcul = Calcul(file_reader)
    return calcul


def test_get_nb_var():
    calcul = init()
    assert calcul.get_nb_var() == 5


def test_get_nb_observation():
    calcul = init()
    assert calcul.get_nb_observation() == 150


def test_get_nb_var_qualitative():
    calcul = init()
    assert calcul.get_nb_var_qualitative() == 1


def test_get_var_qualitative():
    calcul = init()
    var = calcul.get_var_qualitative().strip()
    assert var == '\'Species\''


def test_get_nb_var_quantitative():
    calcul = init()
    assert calcul.get_nb_var_quantitative() == 4


def test_get_var_quantitative():
    calcul = init()
    assert calcul.get_var_quantitative() == '\'Sepal.Length\', \'Sepal.Width\', \'Petal.Length\', \'Petal.Width\''


