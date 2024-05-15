import csv
from io import TextIOWrapper
from myportfolio.models.shares_models import shareIds

def createStocksFromCSV(csv_file):
    #with open(csv_file, mode='r', encoding='ISO-8859-1', errors='replace') as csv_file:
        csv_file_wrapper = TextIOWrapper(csv_file, encoding='utf-8', errors='replace')
        csv_reader = csv.DictReader(csv_file_wrapper, delimiter=';')
        # Skip the first row with the header
        next(csv_reader)
        for row in csv_reader:
            print("Ok: ", row['Bezeichnung'])
            bezeichnung = row['Bezeichnung']
            isin = row['ISIN']
            wkn = row['WKN']
            shareIdObjects = shareIds.objects.filter(isin=isin) | \
                            shareIds.objects.filter(wkn=wkn)
            count = shareIdObjects.count()
            if count > 1:
                raise Exception("Corrupt Data: Multiple Entries for WKN/ISIN")
            elif count == 0:
                new_share_id = shareIds(name=bezeichnung, isin=isin, wkn=wkn)
                new_share_id.save()
            else:
                shareObject = shareIdObjects[0]
                if shareObject.name != bezeichnung:
                    print(bezeichnung)
                    shareObject.alterName = (bezeichnung + "|" + shareObject.alterName)[:64]
                    shareObject.save()
        return True