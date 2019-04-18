import pymongo
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
    string=string.split()

    for words in string:
        if words not in stop_words:
            filtered_sentence.append(words)
    sentence=" ".join(str(x) for x in filtered_sentence)
    return sentence

def posRemoval(string):
    # sentence = []
    string1=nltk.pos_tag(string.split())

    for w,j in string1:
        if(j == 'JJ' or j=='JJR' or j=='JJS' or j=='RB' or j=='RBS' or j=='RBR' or j=='VB' or j=='VBD' or j=='VBN' or j=='VBG' or j=='VBP' or j=='VBZ'):
            sentence="".join(str(w))
    # print(sentence)
    return sentence

def sentiment(score):
    if(score==0):
        return 'neutral'
    if(score>0 and score<0.6):
        return 'positive'
    if(score> 0.6):
        return 'very positive'
    if(score<0 and score> -0.6):
        return 'negative'
    if(score< -0.6):
        return 'very negative'

client = pymongo.MongoClient('localhost', 27017)
db = client['scrapped']
collection = db['data']

# List=[]
# for i in db.data.find():
#     l=[]
#     headLine = word_tokenize(i['headLines'])
#     #whole headLines added to list
#     l.append(i['headLines'])
#     #sentiment scores of the whole headline added
#     l.append(sentimentscores(headLine))
#     #sentiment on basis of the sentiment score of the whole news added to the list
#     l.append(sentiment(sentimentscores(headLine)))
#     #headlines after the stemming process is added to the list
#     l.append(stemming(headLine))
#     #sentiment score of the news after stemming is adde dto the list
#     l.append(sentimentscores(stemming(headLine)))
#     #sentiment on the basis of sentiment score of the stemmed news headline is added to the list
#     l.append(sentiment(sentimentscores(stemming(headLine))))
#     #headline after the removal of stop words is added to the list
#     l.append(stopWords(headLine))
#     #sentiment score of the news after stop words removal is added to the list
#     l.append(sentimentscores(stopWords(headLine)))
#     #sentiment on the basis of the sentiment score of the headline after the stop word removal is added to the list
#     l.append(sentiment(sentimentscores(stopWords(headLine))))
#     #headline after the remvl of selected POS is added to the list
#     l.append(posRemoval(headLine))
#     #sentiment score of the news after the removal of selected POS is added to the list
#     l.append(sentimentscores(posRemoval(headLine)))
#     #sentiment on the basis of the sentiment score of the headlines after the removal of the selected POS is added to the list
#     l.append(sentiment(sentimentscores(posRemoval(headLine))))
#
#     #Now starting the combinations of different features
#
#     #headlines after stemming and stopword removal is added to the list
#     l.append(stopWords(stemming(headLine)))
#     #sentiment score after the stemming and stop words removal is added to the list
#     l.append(sentimentscores(stopWords(stemming(headLine))))
#     #sentiment on the basis of the sentiment scores of the headlines after stemming and stop words removal is added to the list
#     l.append(sentiment(sentimentscores(stopWords(stemming(headLine)))))
#     #headline after selected POS removal and stopword removal is added to the list
#     l.append(stopWords(posRemoval(headLine)))
#     #sentiment score of the headline after selected POS removal and stop word removal is added to the list
#     l.append(sentimentscores(stopWords(posRemoval(headLine))))
#     #senitment on the basis of the sentiment score of the headline after the removal of seleted POS nad stop word removal is added to the list
#     l.append(sentiment(sentimentscores(stopWords(posRemoval(headLine)))))
#     # headlines after stemming and selected POS removal is added to the list
#     l.append(posRemoval(stemming(headLine)))
#     #sentiment score of the headlines after stemming and selected POS removal is added to the list
#     l.append(sentimentscores(posRemoval(stemming(headLine))))
#     #sentiment on the basis of sentiment score of the headlines after stemming and selected POS removal is added to the list
#     l.append(sentiment(sentimentscores(posRemoval(stemming(headLine)))))
#     # headlines after stemming and selected POS and Stopword removal is added to the list
#     l.append(stopWords(posRemoval(stemming(headLine))))
#     # sentiment score of the headlines after stemming and selected POS and stopword removal is added to the list
#     l.append(sentimentscores(stopWords(posRemoval(stemming(headLine)))))
#     # sentiment on the basis of sentiment score of the headlines after stemming and selected POS and Stopword removal is added to the list
#     l.append(sentiment(sentimentscores(stopWords(posRemoval(stemming(headLine))))))
#     #print(l)
#     #print(len(l))
#
#     List.append(l)
# # for a in List:
# #     print(a)
#
# fields = ['Head Lines', 'Sentiment Score (Whole)', 'Sentiment','HeadLines after Stemming', 'Sentiment Score (Stemmed)','Sentiment' , 'Headlines after Stopword Removal ',
#           'Sentiment Score (Stopwords_removed)', 'sentiment', 'Headline after POS Removal', 'Sentiment Score (POS removed)', 'Sentiment', 'HeadLines after Stemming and Stopword removal' ,
#           'Sentiment Score (Stopword Removal(Stemming))', 'Sentiment', 'Headlines after POS Removal and Stopword Removal', 'Sentiment Score (POS Removal(Stemming))',
#            'Sentiment', 'HeadLines after Stemming and POS removal', 'Sentiment Score (POS Removal(Stemming))', 'Sentiment', 'HeadLines after Stemming and POS and Stopword removal',
#           'Sentiment Score (Stopword Removal(POS Removal(Stemming)))', 'Sentiment']
# #print(len(fields))
# with open('Results_updated.csv', 'w', newline='') as csvfile:
#     #creating  a csv writer object
#     csvwriter = csv.writer(csvfile)
#     #writing the fields
#     csvwriter.writerow(fields)
#     # writing the data List
#     csvwriter.writerows(List)