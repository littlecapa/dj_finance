import re
from myportfolio.models.shares_models import shareIds

STOCK_PATTERN_DICT = {
    "WKN_LIST": r"^WKN\n",
}

REPLACE_LIST_DICT = {
    ":": "",
}

def cleanup(shares_list):
    for repl, w in REPLACE_LIST_DICT.items():
        for obj in shares_list:
            obj['name'].replace(repl, w)
    return shares_list

def check_new(share_list):
    for share in share_list:
        if share["name"] != "" and share["wkn"] != "":
            pass

    return share_list

class PatternNotFoundException(Exception):
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

def extract_stocks(text):
    try:
        for type, pattern in STOCK_PATTERN_DICT.items():
            matches = re.findall(pattern, text, re.MULTILINE)
            if matches:
                if type == "WKN_LIST":
                    shares = get_wkn_list(text)
                shares = cleanup(shares)
                shares = check_new(shares)
                return shares
    except PatternNotFoundException as e:
        print(f"Pattern not found: {e.message}")
        return None

def create_share_dict_obj(name, symbol = "", wkn = "", isin = ""):
    share_dict_obj = {
            'name': name,
            'symbol': symbol,
            'wkn': wkn,
            'isin': "",
            'new': True,
            'conflict': False
    }
    return share_dict_obj

def get_wkn_list(text):
    share_json_list = []
    lines = text.split('\n')
    # Iterate through all lines except the first one, which is WKN
    for line in lines[1:]:
        parts = line.split()
        stock_name = ' '.join(parts[:-1])
        wkn_id = parts[-1]
        share_json_list.append(create_share_dict_obj(stock_name, wkn = wkn_id))
    return share_json_list
