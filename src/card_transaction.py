import sys
import random

def transaction(data):
    data__transactin = {
        value: data.pValorTransacao, 
        cupom_number: data.pNumeroCupom,
        control_number: random.randint(0, 99999)
    }
    return data__transactin

sys.modules['__transaction_module__'] = transaction