import os

def load_data(data_path):
    data = []
    for file_name in os.listdir(data_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(data_path, file_name), 'r') as file:
                data.append(file.read())
    return data
