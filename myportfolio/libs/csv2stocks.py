import csv
from io import TextIOWrapper
from myportfolio.models.shares_models import shareIds, transaction
from myportfolio.models.config_models import attrNames
from datetime import datetime
from myportfolio.libs.converter import str2dec

def initReader(source, csv_file):
    config = attrNames.objects.filter(source=source)
    csv_file_wrapper = TextIOWrapper(csv_file, encoding='utf-8', errors='replace')
    csv_reader = csv.DictReader(csv_file_wrapper, delimiter=';')
    # Skip the first row with the header
    next(csv_reader)
    return config[0], csv_reader

def createStocksFromCSV(csv_file, source = "comdirect"):
    config, csv_reader = initReader(source, csv_file)
    for row in csv_reader:
        bezeichnung = row[config.attrName]
        isin = row[config.attrIsin]
        wkn = row[config.attrWkn]
        etf = False
        if row[config.attrEtf] is not None:
            print("ETF: ", row[config.attrEtf])
            if row[config.attrEtf] == "ETF":
                print("Yes")
                etf = True
        currency = "EUR"
        if row[config.attrCurrency] is not None:
            print("Currency: ", currency)
            currency = row[config.attrCurrency]      
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


def importPortfolioFromCSV(csv_file, source = "comdirect"):
    config, csv_reader = initReader(source, csv_file)
    for row in csv_reader:
        isin = row[config.attrIsin]
        share_object = shareIds.objects.filter(isin=isin)
        print(row[config.attrValue], row[config.attrNumber])
        shares_value = str2dec(row[config.attrValue].replace(',', '.'))/100
        numberShares = str2dec(row[config.attrNumber].replace(',', '.'))
        info = "CSV Import"
        date_string = row[config.attrDatum]
        date = datetime.strptime(date_string, "%d.%m.%Y")
        new_transaction = transaction(shares_name=share_object[0], shares_value=shares_value, numberShares=numberShares, info=info, date = date)
        new_transaction.save()