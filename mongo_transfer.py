import pymongo
import csv

client = pymongo.MongoClient("localhost", 27017)
db = client["data_Hammad(new)"]
collection = db['hLines']

handle=open(r"F:\work\fyp2\data\Hammad\AllData.csv")
r=csv.reader(handle)
count=0;
for rows in r:
    print(rows)
    count=count+1

print(count)
