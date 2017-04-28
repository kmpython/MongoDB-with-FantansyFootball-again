import pymongo

class Dbase:
    def setupConnection(self):
        uri = "mongodb://127.0.0.1:27017"
        Mongoclient = pymongo.MongoClient(uri)
        Mongoclient.drop_database('MongoProject')
        database = Mongoclient['MongoProject']
        return database

