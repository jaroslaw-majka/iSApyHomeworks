import json
from livestock import FishStock
from dry_stock import DryStock
from customers import LoyaltyCard


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

    def data_loader(self) -> list:
        try:
            with open('data-files/' + self.json_file_name + '.json', 'r') as load_file:
                retrieved_data = json.load(load_file)
        except FileNotFoundError:
            pass
        else:
            print('File found')
            retrieved_data = json.dumps(retrieved_data)
            retrieved_data = json.loads(retrieved_data)
            loaded_list = []
            for key in retrieved_data:
                if self.json_file_name == 'livestock':
                    loaded_list.append(self.livestock_data_retirever(retrieved_data.get(key)))
                elif self.json_file_name == 'drystock':
                    loaded_list.append(self.drystock_data_retirever(retrieved_data.get(key)))
                elif self.json_file_name == 'customercards':
                    loaded_list.append(self.customers_data_retirever(retrieved_data.get(key)))
            return loaded_list

    def livestock_data_retirever(self, data_to_obj: dict) -> object:
        '''
        Converts input data of dict type to a FishStock class instance
        :param data_to_obj: dict object
        :return: FishStock class instance
        '''
        return FishStock(data_to_obj['name'], data_to_obj['origin'], data_to_obj['amount'], data_to_obj['freshwater'])

    def drystock_data_retirever(self, data_to_obj) -> object:
        '''
        Converts input data of dict type to a DryStock class instance
        :param data_to_obj: dict object
        :return: DryStock class instance
        '''
        return DryStock(data_to_obj['name'], data_to_obj['item_type'], data_to_obj['brand'], data_to_obj['stock'])

    def customers_data_retirever(self, data_to_obj) -> object:
        '''
        Converts input data of dict type into a LoyaltyCard class instance.
        Class attributes need to be provided step by step because constructor of a class accepts only one attribute.
        :param data_to_obj: dict object
        :return: LoyaltyCard class isntance
        '''
        converted_object = LoyaltyCard(data_to_obj['name'])
        converted_object.card_idx = data_to_obj['card_idx']
        converted_object.collected_points = data_to_obj['collected_points']
        converted_object.purchase_history = data_to_obj['purchase_history']
        LoyaltyCard.next_card_idx = data_to_obj['card_idx'] + 1
        return converted_object
