import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import pymongo


def getNewsTitles(url):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['scrapped']
    collection = db['data']
    pagesUrl = ["page/1/", "page/2/", "page/3/", "page/4/", "page/5/"];
    links = []
    titles = []
    headLines = []
    j=0
    for page in pagesUrl:

        req = urllib.request.Request(url + page, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(
            req).read()  # read is used so whole document is obtained in a singe big string with a new line character at the end of each line
        soup = BeautifulSoup(html, 'html.parser')

        # retrieve all the anchor tags
        # anchor tags=div having class singleTitle in an html page
        # that is we want to extracts all the links from the page

        tags = soup('div', attrs={"class": "singletitle"})

        for tag in tags:
            # print('TAG:', tag)


            link = tag.find('a')
            print('links: ', link['href'])
            print('title: ', link['title'])
            y = re.sub('Permanent Link to ', '', link['title'])
            print('headiLine is: ', y)
            links.append(link['href'])
            headLines.append(y)

        #    db.data.update({'_id': client._id}, {set} )

            #db.data.remove({"number":j})    removing rows on basis of a column
            #for new data insertion
         #   new_info = collection.insert_one({
         #       "links": str(link['href']),
         #       "titles": str(link['title']),
         #       "headLines": str(y)
         #       "number":j
          #})

            titles.append(y)
            print('\n')
    print('no of records = '+str(collection.count()))
   # print(db.data.find())
    wordset = set()

    for i in db.data.find():
        k=j+1
        newsHead=i['headLines'].split(' ') #tokenizer
        wordset=wordset.union(newsHead) #using sets to remove duplicates
        #wordset=wordset.union(set(newsHead))
        print(str(k)+' '+i['headLines'])
        print(headLines[j])
        j=j+1

    print(len(wordset))


getNewsTitles('http://www.brecorder.com/pakistan/')
