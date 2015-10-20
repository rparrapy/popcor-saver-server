from pymongo import MongoClient

class mongoHandler():
    def connect(self):
        client = MongoClient()
        db = client['popcorn-saver']
        #print db
        cursor = db.movies.find()
        cursor = db.movies.find({"year": {"$gt": 2014}})
        #cursor = db.movies.find({"movieId": "27266"})
        return cursor
        # for document in cursor:
        #     #document.year
        #     print(document['title'])
    def createTweetField(self):
        return
    def splitTitle(self, titleName):
        return titleName.split("(")[0]


# if __name__ == '__main__':
#     collector = queryDB()
#     #collector.connect()
#     print collector.splitTitle("Rodrigo (18221)")
