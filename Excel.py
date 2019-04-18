import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client["data_Hammad(new)"]
collection = db["allFeatures_new"]
data = db.allFeatures_new.find()
import csv

List = []
for i in data:
    l = []
    l.append(i["News"])
    l.append(i["Sentiment"])
    l.append(i["stopwordsRemoved"])
    l.append(i["stemming"])
    l.append(i["POSRemoval"])
    l.append(i["stemming_pos"])
    l.append(i["pos_stemming"])
    l.append(i["Stopwords_stemming"])
    l.append(i["pos_stopWords"])
    l.append(i["stopWords_pos"])
    l.append(i["stemming_stopwords"])
    l.append(i["all_Features"])

    List.append(l)

fields = ['Head Lines', 'Sentiment', 'Stemmed', 'StopWords Removed', 'PosRemoval', 'stemming_posRemoval',
          'PosRemoval_stemming', 'Stopwords_stemming',
          'Pos_StopWords', 'StopWords_Pos', 'Stemming_StopWords', 'All Features']
# print(len(fields))
with open('Features Extracted.csv', 'w') as csvfile:
    # creating  a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data List
    csvwriter.writerows(List)