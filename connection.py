from pymongo import MongoClient
import pymongo

#database is set up
def database_setup():

    client = MongoClient("mongodb://suraj29:pict123@ds033175.mongolab.com:33175/arduino-db")
    print client

    db = client['arduino-db']
    print db

    return db


#here user authentication is done and then rendered
def get_auth_details(db):
	auth=db.collector_AUTH
	document=auth.find().sort([("_id",pymongo.DESCENDING)]).limit(1)
	print type(document)
	for doc in document:
		return [str(doc['username']),str(doc['password'])]	






#document is inserted in MONGOLAB .it is received from /
def insert__sensor_document(s,db):
    garbageCollection = db.garbage
    
    #print 'db-connected'
    doc = s
    

    garbage_id = garbageCollection.insert_one(doc).inserted_id

    return garbage_id




#final sequence is received from the server of the path to be followed and is inserted in the database  .Its received from /tsp/areaid
def insert_sequence_document(sequence,db):
	
	sequence_path=db.collection_sequence
	doc=sequence
	
	a=sequence_path.insert_one(doc).inserted_id
	
	
	return a




#document is fetched based  in descending order of the timestamp and fed to brute.py
def get_document(areaid,db,canid):
	garbageCollection=db.garbage
	
	document=garbageCollection.find({"areaid":int(areaid) ,"canid":int(canid)}).sort([("timestamp",pymongo.DESCENDING)]).limit(1)
	for doc in document:
		return doc['level']
	





#javascript browser client will get the sequence to be mapped   .request is received from  /sequence
def get_sequence(db):
	sequence=db.collection_sequence
	
	document=sequence.find().sort([("_id",pymongo.DESCENDING)]).limit(1)
	
	for doc in document:
		return str(doc['sequence'])
	



if __name__ == '__main__':
   db = database_setup()
   print insert_document("50",db)


