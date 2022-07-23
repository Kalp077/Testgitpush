import pymongo
client = pymongo.MongoClient("mongodb+srv://<username>:<Kshevale0077>@cluster0.mib8i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "kalpesh",
    "email" : "kalpesh.shevale@",
    "surname" : "shevale"}

db1 = client['mongotest']
coll = db1['test1']
coll.insert_one(d )




