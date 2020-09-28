import datetime
import os

from script.file_reader import FileReader

PATH = os.getcwd() + "/data/iris.csv"


def test_display_size_file():
    file_reader = FileReader(PATH)
    assert file_reader.display_size_file() == '4821'


def test_display_encoding_file():
    file_reader = FileReader(PATH)
    assert file_reader.display_encoding_file() == 'ascii'


def test_display_date_modif_file():
    file_reader = FileReader(PATH)
    assert file_reader.display_date_modif_file() == datetime.datetime(2018, 11, 2, 21, 13, 10, 192678)


def test_get_data():
    file_reader = FileReader(PATH)
    assert file_reader.get_data() is not None
