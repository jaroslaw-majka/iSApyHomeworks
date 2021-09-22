import json


class DataManager:
    def __init__(self, list_for_saving: list, json_file_name: str):
        self.list_for_saving = list_for_saving
        self.json_file_name = json_file_name
        self.converted_dict = self.dict_converter()

    def dict_converter(self) -> dict:
        '''
        Converts passed list into a dict ready to be saved in a JSON file
        :return: dict
        '''
        holder_dict = {}
        for i in range(len(self.list_for_saving)):
            holder_dict[self.list_for_saving[i].name] = vars(self.list_for_saving[i])
        return holder_dict

    def data_writer(self) -> None:
        '''
        uses the converted dict and saves it in a json file
        '''
        with open('data-files/' + self.json_file_name + '.json', 'w') as write_file:
            json.dump(self.converted_dict, write_file)

    def data_loader(self):
        with open(self.json_file_name + '.json', 'r') as load_file:
            retrieved_data = json.load(load_file)
        retrieved_data = json.dumps(retrieved_data)
        retrieved_data = json.loads(retrieved_data)
        # TODO convert to obj and save in a list
        for key in retrieved_data:
            print(type(retrieved_data.get(key)))
