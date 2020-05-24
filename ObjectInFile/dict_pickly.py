import pickle
from pathlib import Path


class ClassRules:
    """This class for create BD type dist"""

    def __init__(self):
        self.path_to_file = 'data_file.data'
        data_dict = {}
        if not Path(self.path_to_file).exists():
            with open(self.path_to_file, 'wb') as f:
                pickle.dump(data_dict, f)
        else:
            with open(self.path_to_file, 'rb') as f:
                try:
                    data_dict = pickle.load(f)
                except Exception:
                    with open(self.path_to_file, 'wb') as f:
                        pickle.dump(data_dict, f)

    def __write_data(self, data_dict):
        self.data_dict = data_dict
        with open(self.path_to_file, 'wb') as f:
            pickle.dump(data_dict, f)

    def get_data(self):
        with open(self.path_to_file, 'rb') as f:
            data_dict = pickle.load(f)
        return data_dict

    def add_data(self, dict_data: dict):
        self.dist_data = dict_data
        dict_file = self.get_data()
        dict_file.update(self.dist_data)
        self.__write_data(dict_file)

    def delete_data(self):
        pass
