from datetime import datetime
from decimal import Decimal

def str2dec(string):
    string = string.replace('.', '')
    string = string.replace(',', '.')
    value = Decimal(string)
    return value

def formatGerNumberStr(number_str):
    # Replace "." with ","
    number_str = number_str.replace('.', ',')

    # Split the string into the integer part and the decimal part
    if ',' in number_str:
        integer_part, decimal_part = number_str.split(',')
    else:
        integer_part, decimal_part = number_str, ''

    # Ensure max 2 digits after ","
    decimal_part = decimal_part[:2]

    # Reverse the integer part for easier grouping
    integer_part = integer_part[::-1]

    # Group digits in threes
    grouped_integer = '.'.join([integer_part[i:i+3] for i in range(0, len(integer_part), 3)])

    # Reverse back to the original order
    grouped_integer = grouped_integer[::-1]

    # Combine integer and decimal parts
    if not decimal_part:
        formatted_number = f"{grouped_integer},00"
    else:
        if len(decimal_part) == 1:
            decimal_part = decimal_part+"0"
        formatted_number = f"{grouped_integer},{decimal_part}"

    return formatted_number
