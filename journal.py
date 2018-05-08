"""
This is the Journal module, for saving and loading data.
"""

import os

def load(name):
    """
    This method creates and loads a new Journal.

    :param name: This is the base name of the Journal to load.
    :return: The Journal data is imported from the file and loaded here.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    """
    This method saves the data that has been input by the user.
    :param name: This is the base name of the Journal being saved.
    :param journal_data: This is the information created within the Journal that will be saved.
    :return: The data that has been inputted by the user is saved into the 'Journals' directory.
    """
    filename = get_full_pathname(name)
    print('Saving to: {}'.format(filename))
    with open(filename, 'w') as file:
        for entry in journal_data:
            file.write(entry + '\n')


def get_full_pathname(name):
    """
    The pathname to save and load the Journal files from.
    :param name: The name of the file to save/load.
    :return: The pathname is returned to save the file to or load the file from.
    """
    filename = os.path.abspath(os.path.join('Journals', name + '.jrl'))
    return filename


def add_entry(text,journal_data):
    """
    An entry is added to the active Journal.
    :param text: the text that the user has inputted
    :param journal_data: the already existing journal data
    :return: the existing journal is appended to add the users input
    """
    journal_data.append(text)