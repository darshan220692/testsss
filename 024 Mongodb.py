import pymongo

client = pymongo.MongoClient("mongodb://ineuron:Rudra22@ac-12dgp8j-shard-00-00.hyuwequ.mongodb.net:27017,ac-12dgp8j-shard-00-01.hyuwequ.mongodb.net:27017,ac-12dgp8j-shard-00-02.hyuwequ.mongodb.net:27017/?ssl=true&replicaSet=atlas-ahoqqf-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

db1 = client['mongotest']
coll = db1['test']
coll1 = db1['test1']
coll2 = db1['test2']

my_co = ['coll', 'coll1', 'coll2']
for my_cols in my_co:
    record = my_cols.find_one()
    for i in record:
        print(i)

# record = coll.find()
# for i in record:
#     print (i)

# record = coll.find({"surname":"Kalamkhede"})
# for i in record:
#     print(i)
#
# all_data_under_database = db1.find()
#
# for i in all_data_under_database:
#     print(i)

my_co = ['coll', 'coll1', 'coll2']
for my_cols in my_co:
    record = my_cols.find()
    for i in record:
        print(i)