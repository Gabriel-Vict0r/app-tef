import sys
import random


class Data:
    def __init__(self, value, cupom_number, control_number):
        self.value = value
        self.cupom_number = cupom_number
        self.control_number = control_number

def transaction(data):
    id = random.randint(0, 99999)
    #print(data['pValorTransacao'])
    data_transaction = Data(data['pValorTransacao'], data['pNumeroCupom'], id)
    print(data_transaction)
    return data_transaction

sys.modules['__transaction_module__'] = transaction