from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["Stock_Information"]
collection = db["news"]

data=db.news.find()
doc_complete=["hey you there i am using whatsapp. what about you?"]

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]
print(doc_clean)

# Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
dictionary = corpora.Dictionary(doc_clean)
# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=15, id2word = dictionary, passes=2)

print(ldamodel.print_topics(num_topics=15, num_words=7))

print(ldamodel.log_perplexity(doc_term_matrix))

for i, row in enumerate(ldamodel[doc_term_matrix]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = " ".join([word for word, prop in wp])

            else:
                break
print(topic_keywords)
# i=0
# while i <(len(ldamodel.id2word)):
#     print(ldamodel.id2word[i])
#     print(i)
#     i=i+1
