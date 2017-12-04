import pymongo
from collections import Counter
import math

def wordCount(list):
    count=len(list)
    return count

def termCount(list):
    count = dict()

    for word in list:
        #print(word)
        if word not in count:
            count[word] = 1
           # print(count[word])
        else:
            count[word] = count[word] + 1

    return count


def computeTF(tFreq, totalWords): # count term frequency in the dictionary
    tf= tFreq/totalWords
    return tf

def computeIDF(wordset1):
    idf=dict()
    for term, value in Counter(wordset1).items():
       # print('idf of term ' + term + ' is')
       # print(value)
       # print(math.log(totalNews / value))
        idf[term]= math.log(totalNews / value)
    return idf.items()


client = pymongo.MongoClient('localhost', 27017)
db = client['scrapped']
collection = db['data']

totalNews=0
Dictionary=dict()
y=0
z=''
wordset=list()
wordset1=list()
tf_idf=dict()
for i in db.data.find():
    totalNews=totalNews+1
    newsHead = i['headLines'].split(' ')  # tokenizer
   # print(i['headLines'])
   # print(wordCount(newsHead))
    tDoc = termCount(newsHead)
    wordset.append(newsHead)
    #for printing the items of the dictionary
    for (k, v) in tDoc.items():
        print('term frequency of '+k +' in news number '+str(totalNews)+' is')
        print(computeTF(v, wordCount(newsHead)))
        z=k
        y=v
        wordset1.append(k)

#calling tf and idf function
for i in db.data.find():
    newsHead = i['headLines'].split(' ')  # tokenizer
   # print(i['headLines'])
   # print(wordCount(newsHead))
    tDoc = termCount(newsHead)
    #for printing the items of the dictionary
    for (k, v) in tDoc.items():
        print('term frequency of '+k +' in news number '+str(totalNews)+' is')
        tf=computeTF(v, wordCount(newsHead))
        print(tf)
        for term, idf in computeIDF(wordset1):
            if k== term:
                print('idf of ' + term + ' is ' + str(idf))
                tf_idf[k]=tf*idf

print('total number of news is '+str(totalNews))
print(wordset)
print(len(wordset))
print(wordset1)
print(len(wordset1))
print(Counter(wordset1))
print(len(Counter(wordset1)))


for word, value in tf_idf.items():
    print(word, value)

print(len(tf_idf))