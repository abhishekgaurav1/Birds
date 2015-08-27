'''
Created on 27-Aug-2015

@author: Abhishek.Gaurav
'''
from bson.objectid import ObjectId

class DbHandler:
    def get_db(self):
        """This function will make db connection and return connection object"""
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.birds
        return db
    
    def add_bird(self,birdJson):
        """This function will add an object to DB"""
        try:
            db = self.get_db()
            data= db.birds.insert(birdJson)
            print data
            return data
        except Exception, e:
            print e
            return {}
        
    def get_bird(self,birdId):
        """This function will find an object for a given object ID"""
        db = self.get_db()
        return db.birds.find_one(ObjectId(birdId))
    
    def get_all_birds(self):
        """This function will find all entry which has visible value set as true"""
        try:
            db = self.get_db()
            data = []
            for i in db.birds.find():
                if i["properties"]["visible"]["type"]:
                    data.append(i)
            return data
        except Exception,e:
            print e
            return {}
    
    def get_country(self):
        db = self.get_db()
        return db.birds.find()
    
    def delete_bird(self,id):
        """This function will delete an entry for a given object id"""
        db = self.get_db()
        db.birds.remove(ObjectId(id))

if __name__ == "__main__":

    db = DbHandler() 
    print db.get_all_birds()
    #db.delete_bird("55df4b6cbd9a732fa0aa5247")
    #ss =  db.get_country()
    #for i in ss:
    #    print i