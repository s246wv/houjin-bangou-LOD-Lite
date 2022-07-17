from fileinput import filename
import pandas as pd 
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import XSD 
import sys

args = sys.argv
filename = args[1]
# filename = "00_zenkoku_all_20220630_000.csv" ##ここを変えてね．
df=pd.read_csv(filename, sep=",",quotechar='"', dtype=str) ##コンマ区切り，クオータはダブルクオーテーションを想定．

## グラフ作ります．
g = Graph()
houjin = Namespace('https://github.com/s246wv/MLIT_bidding_info/houjin-bangou/')

for index, row in df.iterrows():
    keys = row.keys()
    
    if(pd.isnull(row['sequenceNumber'])):
        print("error: no sequence number. i hope this line never be referred.")
        break
    else:
        for key in keys:
            if(pd.isnull(row[key])):
                pass ## 値がない人はスキップされます．
            else:
                sequenceNumber = str(row['sequenceNumber'])
                if(key == 'corporateNumber'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'process'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'correct'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'updateDate'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.date)))
                elif(key == 'changeDate'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.date)))
                elif(key == 'name'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'nameImageId'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'kind'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'prefectureName'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'cityName'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'streetNumber'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'addressImageId'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'prefectureCode'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'cityCode'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'postCode'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(str(row[key]), datatype=XSD.string)))
                elif(key == 'addressOutside'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'addressOutsideImageId'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'closeDate'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.date)))
                elif(key == 'closeCause'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'successorCorporateNumber'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'changeCause'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'assignmentDate'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.date)))
                elif(key == 'latest'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                elif(key == 'enName'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='en')))
                elif(key == 'enPrefectureName'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='en')))
                elif(key == 'enCityName'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='en')))
                elif(key == 'enAddressOutside'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='en')))
                elif(key == 'furigana'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], lang='ja')))
                elif(key == 'hihyoji'):
                    g.add((URIRef(houjin + sequenceNumber), URIRef(houjin + key), Literal(row[key], datatype=XSD.string)))
                else:
                    pass
                

g.serialize(filename + '.ttl', format='turtle')