import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import svm
# from sklearn.svm import LinearSVC
import pymongo

client = pymongo.MongoClient("localhost", 27017)
# db = client["data_Hammad"]
db = client["data_Hammad(new)"]
# collection = db["hLines"]
collection=db["allFeatures_new"]

# data=db.hLines.find()
data=db.allFeatures_new.find()
df = pd.DataFrame(list(data), columns = ["News","Sentiment"])
df = df.sample(frac=1).reset_index(drop=True)

df_x=df["News"]
df_y=df["Sentiment"]
# initializing count vectorizer
cv = CountVectorizer()
#print(df["pos_stemming"])
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=0)
x_traincv=cv.fit_transform(x_train)
a=x_traincv.toarray()
x_testcv=cv.transform(x_test)

# svm algo
supportvm = svm.SVC(kernel='linear', C=1, gamma=1)

y_train=y_train.astype('int')
supportvm.fit(x_traincv,y_train)
testmessage=x_test.iloc[0]
predictions=supportvm.predict(x_testcv)
a=np.array(y_test)
# count=0
# for i in range (len(predictions)):
#     if predictions[i]==a[i]:
#         count=count+1.0
#
#
# print("The accuracy is ")
# print((count/len(predictions))*100)

count=0
falsePositve=0
falsenegative=0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1.0
    if (predictions[i]>0) and (a[i]==0 or a[i]<0):
        falsePositve=falsePositve+1.0
    if (predictions[i] < 0) and (a[i] == 0 or a[i] > 0):
        falsenegative=falsenegative+1.0


print("The accuracy is ")
print((count/len(predictions))*100)

print("false positive is ")
print((falsePositve/len(predictions))*100)


print("false negative is ")
print((falsenegative/len(predictions))*100)
