from pymongo import MongoClient

CONNECTION_STRING = "mongodb://suraj29:pict123@ds033175.mongolab.com:33175/arduino-db"

DATABASE_NAME = "arduino-db"

GARBAGE_CANS_COLLECTION = "garbage-cans"


class Database:
    def __init__(self,connection_string):
        self.mongoclient = MongoClient(connection_string)

    def connect_to_database(self,database_name):
        self.database = self.mongoclient[database_name]

    def connect_to_collection(self,collection_name):
        self.collection = self.database[collection_name]



if __name__ == '__main__':
    d = Database(CONNECTION_STRING)
    d.connect_to_database(DATABASE_NAME)
    d.connect_to_collection(GARBAGE_CANS_COLLECTION)

    #print d.collection.insert_one({'canid':2,'level':15,'areaid':001,'location':{'xcord':43.73,'ycord':59.88}}).inserted_id


 #   d.collection.insert_many([{'canid':3,'level':6,'areaid':001,'location':{'xcord':45.55,'ycord':67.77}},{'canid':4,'level':9,'areaid':001,'location':{'xcord':65.73,'ycord':90.88}},{'canid':5,'level':7,'areaid':001,'location':{'xcord':55.73,'ycord':60.88}}])


    for doc in d.collection.find():
        print doc
