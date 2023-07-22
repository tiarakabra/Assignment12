import pickle

def read_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

def write_data(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)
