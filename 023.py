import pymongo

client = pymongo.MongoClient("mongodb://ineuron:Rudra22@ac-12dgp8j-shard-00-00.hyuwequ.mongodb.net:27017,ac-12dgp8j-shard-00-01.hyuwequ.mongodb.net:27017,ac-12dgp8j-shard-00-02.hyuwequ.mongodb.net:27017/?ssl=true&replicaSet=atlas-ahoqqf-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Darshan",
    "surname":"Kalamkhede",
    "emailID":"darshan.kalamik@gamil.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)