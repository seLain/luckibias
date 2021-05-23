import json

def load_649():

    with open('database/tw_lottery_649.json', 'r') as f:
        data_649 = json.load(f)
        return data_649

    return None