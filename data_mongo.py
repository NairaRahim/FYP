import pymongo
import pandas as pd

client = pymongo.MongoClient("localhost", 27017)
db = client["lsdda(data)"]
collection = db['artist']

#db.data.update({'_id': client._id}, {set} )

#df=pd.read_excel(r"F:\work\fyp2\pycharm\data.xls", sheetname=0)

#df=pd.read_excel(r"F:\work\fyp2\data\Hammad\AllData.xlsx", sheetname=0)
df=pd.read_excel(r"F:\work\modules\LSDDA\cw\data\TopHitMusicSongs.csv", sheetname=0)


#df=pd.read_excel(r"F:\work\fyp\untitled\Results(newData).xlsx", sheetname=0)
#df = df.sample(frac=1).reset_index(drop=True)
#print(df)
#for fyp
# df.loc[df["Sentiment"]=='Positive',"Sentiment",]=1
# df.loc[df["Sentiment"]=='Negative',"Sentiment",]=-1
# df.loc[df["Sentiment"]=='Neutral',"Sentiment",]=0

#print(df)
# df_news=df["News"]
# df_sentiment=df["Sentiment"]
## df_news=df["News"]
## df_sentiment=df["Sentiment"]
# df_hStemming=df["hStemming"]
# df_hStopWords=df["hStopWords"]
# df_hPOS=df["hPOS"]
# df_hStStopWords=df["hStStopWords"]
# df_hPOSStopWords=df["hPOSStopWords"]
# df_hStPOS=df["hStPOS"]
# df_allFeatures=df["allFeatures"]

sentiment=dict()
print(len(df_news))
# for i in range(len(df_news)):
#     sentiment[df_news[i]]=df_sentiment[i]
#
print(len(df_sentiment))
for i in range(len(df_news)):
    print(df_news[i])
    print(df_sentiment[i])
#use to enter data
    # new_info = db.hLines.insert_one({
    #     "News": df_news[i],
    #     "Sentiment": df_sentiment[i]
    #     # "hStemming": df_hStemming[i],
    #     # "hStopWords": df_hStopWords[i],
    #     # "hPOS": df_hPOS[i],
    #     # "hStStopWords": df_hStStopWords[i],
    #     # "hPOSStopWords": df_hPOSStopWords[i],
    #     # "hStPOS": df_hStPOS[i],
    #     # "allFeatures": df_allFeatures[i]
    # })
#
# #     #used to remove data from a collection
#     new_info = db.hLines.remove({
#         "News": df_news[i],
#         "Sentiment": df_sentiment[i]
#     })
#
# print("length of dictionary is ")
# print(len(sentiment))