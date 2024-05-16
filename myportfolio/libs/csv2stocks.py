import csv
from io import TextIOWrapper
from myportfolio.models.shares_models import shareIds
from myportfolio.models.config_models import attrNames

def createStocksFromCSV(csv_file, source = "comdirect"):
    config = attrNames.objects.filter(source=source)
    print("Config: ", config[0], config.count())
    csv_file_wrapper = TextIOWrapper(csv_file, encoding='utf-8', errors='replace')
    csv_reader = csv.DictReader(csv_file_wrapper, delimiter=';')
    # Skip the first row with the header
    next(csv_reader)
    for row in csv_reader:
        print("Ok: ", row[config[0].attrName])
        bezeichnung = row[config[0].attrName]
        isin = row[config[0].attrIsin]
        wkn = row[config[0].attrWkn]
        etf = False
        if row[config[0].attrEtf] is not None:
            print("ETF: ", row[config[0].attrEtf])
            if row[config[0].attrEtf] == "ETF":
                print("Yes")
                etf = True
        currency = "EUR"
        if row[config[0].attrCurrency] is not None:
            print("Currency: ", currency)
            currency = row[config[0].attrCurrency]      
        shareIdObjects = shareIds.objects.filter(isin=isin) | \
                        shareIds.objects.filter(wkn=wkn)
        count = shareIdObjects.count()
        if count > 1:
            raise Exception(f"Corrupt Data: Multiple Entries for WKN/ISIN {shareIdObjects[0].name} {shareIdObjects[1].name} ")
        elif count == 0:
            new_share_id = shareIds(name=bezeichnung, isin=isin, wkn=wkn, isEtf = etf, currency = currency)
            new_share_id.save()
        else:
            shareObject = shareIdObjects[0]
            shareObject.isEtf = etf
            shareObject.currency = currency
            if shareObject.name != bezeichnung:
                print(bezeichnung)
                shareObject.alterName = (bezeichnung + "|" + shareObject.alterName)[:64]
            shareObject.save()
    return True