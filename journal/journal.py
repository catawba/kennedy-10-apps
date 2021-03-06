import os

def load(name):
    '''
    This method creats and loads a new journal.

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    '''
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return []


def save(name, journal_data):
    filename =  get_full_pathname(name)
    print('.....saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.txt'))


def add_entry(text, journal_data):
    journal_data.append(text)