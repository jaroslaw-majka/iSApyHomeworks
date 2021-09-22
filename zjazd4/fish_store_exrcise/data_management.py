import json


class DataManager:
    def __init__(self, list_for_saving):
        self.list_for_saving = list_for_saving
        self.converted_dict = self.dict_converter()

    def dict_converter(self):
        holder_dict = {}
        for i in range(len(self.list_for_saving)):
            holder_dict[self.list_for_saving[i].name] = vars(self.list_for_saving[i])
        return holder_dict

    def data_writer(self):
        with open('stock_database.json', 'w') as write_file:
            json.dump(self.converted_dict, write_file)

    def data_loader(self):
        with open('stock_database.json', 'r') as load_file:
            retrieved_data = json.load(load_file)
        retrieved_data = json.dumps(retrieved_data)
        retrieved_data = json.loads(retrieved_data)
        # TODO convert to obj and save in a list
        for key in retrieved_data:
            print(type(retrieved_data.get(key)))
