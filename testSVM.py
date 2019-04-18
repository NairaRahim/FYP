# import numpy as np
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cross_validation import train_test_split
# from sklearn import svm
# import pymongo
# import pickle
# from svm_tfIdf_vector import svm
# from pre_processingData import stemming, stopWords,posRemoval
# from sklearn.pipeline import Pipeline
#
#
# string="Hello this is testing"
# stem=stemming(string)
# stemmed="".join(str(x) for x in stem)
#
# stopwordRemoval=stopWords(stemmed)
# stopwordRemoved="".join(str(x) for x in stopwordRemoval)
#
# POS=posRemoval(stopwordRemoved)
# POStag="".join(str(x) for x in POS)
# List=POStag.split()
# df = pd.DataFrame(list(List))
# print(df)
# cv =  TfidfVectorizer(min_df=1,stop_words='english')
# X=cv.fit_transform(df)
# print(X)
#
# # filename = 'finalized_model.sav'
# # loaded_model = pickle.load(open(filename, 'rb'))
# # predictions=loaded_model.predict(X)


#####  testing begind here


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import svm
import pymongo
import pickle

client = pymongo.MongoClient("localhost", 27017)
#db = client["data_Hammad"]
db = client["data_Hammad(new)"]
# collection = db["hLines"]
collection = db["allFeatures_new"]
data=db.allFeatures_new.find()

df = pd.DataFrame(list(data), columns = ["all_Features","Sentiment"])
df = df.sample(frac=1).reset_index(drop=True)

df_x=df["all_Features"]
df_y=df["Sentiment"]
# initializing tf_idf vectorizor
cv =  TfidfVectorizer(min_df=1,stop_words='english')

s = "Hello! My name is naira and I am "
u = unicode(s, "utf-8")

x_train=df_x[0:1200]
y_train=df_y[0:1200]
x_test=u

print(type(u))

x_traincv=cv.fit_transform(x_train)

x_testcv=cv.transform([x_test])

supportvm = svm.SVC(kernel='linear', C=1, gamma=1)
y_train=y_train.astype('int')
supportvm.fit(x_traincv,y_train)

filename = 'finalized_model.sav'
pickle.dump(supportvm, open(filename, 'wb'))

predictions=supportvm.predict(x_testcv)

print(predictions)