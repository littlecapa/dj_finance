def extract_stocks(text):
    lines = text.strip().split("\n")
    key_name = lines[0]
    # Extrahieren der WKNs
    keys = [line.split()[-1] for line in lines[1:]]
    stock_part_list = [line.split()[0] for line in lines[1:]]

    stock_names = []
    for parts in stock_part_list:
        string = " ".join(parts).replace(":", "")
        stock_names.append(string)

    return key_name, dict(zip(keys, stock_names))