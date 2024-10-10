import sys
import random


class Data:
    def __init__(self, value, cupom_number, control_number, type_card):
        self.value = value
        self.cupom_number = cupom_number
        self.control_number = control_number
        self.type_card = type_card

    def to_dict(self):
        return { 
            'value': self.value,
            'cupom_number': self.cupom_number,
            'control_number': self.control_number, 
            'type_card': self.type_card
        }

def transaction(data):
    id = random.randint(0, 99999)
    #print(data['pValorTransacao'])
    data_transaction = Data(data['pValorTransacao'], data['pNumeroCupom'], id, data['pTipoCartao'])
    #print(data_transaction.value)
    return data_transaction.to_dict()

sys.modules['__transaction_module__'] = transaction