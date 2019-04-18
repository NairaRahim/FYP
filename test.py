import csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import csv

def sentimentscores(string):
    sid = SentimentIntensityAnalyzer()
    score = 0
    #print(string)

    for words in string:
        # print(words)
        score = score + sid.polarity_scores(words)['compound']
    return score


def stemming(string):
    ps = PorterStemmer()
    stemmed_sentence = []
    for words in string:
        stemmed_sentence.append(ps.stem(words))
    return stemmed_sentence

def stopWords(string):
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in string if not w in stop_words]
    filtered_sentence = []

    for words in string:
        if words not in stop_words:
            filtered_sentence.append(words)

    return filtered_sentence

def posRemoval(string):
    sentence = []
    string=nltk.pos_tag(string)

    for w,j in string:
        if(j == 'JJ' or j=='JJR' or j=='JJS' or j=='RB' or j=='RBS' or j=='RBR' or j=='VB' or j=='VBD' or j=='VBN' or j=='VBG' or j=='VBP' or j=='VBZ'):
         sentence.append(w)
    return sentence

def sentiment(score):
    if(score==0):
        return 'Neutral'
    if(score>0 and score<0.6):
        return 'Positive'
    if(score> 0.6):
        return 'very positive'
    if(score<0 and score> -0.6):
        return 'Negative'
    if(score< -0.6):
        return 'very negative'

#handle=open("Sentiment(TrainingDataSemevalTestingDataPSX).csv")
handle=open(r"F:\work\fyp2\data\Hammad\AllData.csv")
data=[]
r=csv.reader(handle)
count=0
c=0
List=[]
for rows in r:
    l=[]
    # print('news')
    # print(rows[0])
    # print('result hammad')
    # print(rows[1])
    # print('result naira')
    # print(sentiment(sentimentscores(stemming(rows[1]))))
    # # if(rows[6]==sentiment(sentimentscores(posRemoval(stemming(rows[1]))))):
    # #     print('success')
    # #     count=count+1;
    # #
    # # if(sentiment(sentimentscores(stemming(stopWords(rows[1]))))!='Neutral'):
    # #     print('we have negative')
    # #     c=c+1
    l.append(rows[0])
    l.append(rows[1])
    l.append(sentiment(sentimentscores(stemming(rows[0]))))
    l.append(sentiment(sentimentscores(stopWords(rows[0]))))
    l.append(sentiment(sentimentscores(posRemoval(rows[0]))))
    l.append(sentiment(sentimentscores(stopWords(posRemoval(rows[0])))))
    l.append(sentiment(sentimentscores(stemming(posRemoval(rows[0])))))
    l.append(sentiment(sentimentscores(posRemoval(stopWords(rows[0])))))
    l.append(sentiment(sentimentscores(posRemoval(stemming(rows[0])))))
    l.append(sentiment(sentimentscores(stopWords(posRemoval(stemming(rows[0]))))))

    List.append(l)


print(count)
print(c)


fields = ['Head Lines', 'Sentiment_Hammad', 'Sentiment_Stemming','Sentiment_sopwords','Sentiment_posRemoval','Sentiment_stopwords_posRemoval','Sentiment_stemming_posRemoval',
          'Sentiment_posRemoval_stopwords','Sentiment_posRemoval_stemming','Sentiment_allfeatures']
#print(len(fields))
with open('Comaprison(new).csv', 'w') as csvfile:
    #creating  a csv writer object
    csvwriter = csv.writer(csvfile)
    #writing the fields
    csvwriter.writerow(fields)
    # writing the data List
    csvwriter.writerows(List)