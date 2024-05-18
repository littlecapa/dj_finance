from datetime import datetime
from decimal import Decimal

def str2dec(string):
    string = string.replace('.', '')
    string = string.replace(',', '.')
    value = Decimal(string)
    return value