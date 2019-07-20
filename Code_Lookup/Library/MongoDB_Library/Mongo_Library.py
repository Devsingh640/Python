import pymongo  # imported pymongo library to use mongose database.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # creating connection to mongodb.
mydb = myclient["mydatabase"]    # creating database
mycol = mydb["customers"]  #creading collection.

mylist =    [
                { "_id": 15, "name": "John", "address": "Highway 37"},
                { "_id": 16, "name": "Peter", "address": "Lowstreet 27"},
                { "_id": 17, "name": "Amy", "address": "Apple st 652"},
                { "_id": 18, "name": "Hannah", "address": "Mountain 21"},
                { "_id": 19, "name": "Michael", "address": "Valley 345"},
                { "_id": 20, "name": "Sandy", "address": "Ocean blvd 2"},
                { "_id": 21, "name": "Betty", "address": "Green Grass 1"},
                { "_id": 22, "name": "Richard", "address": "Sky st 331"},
                { "_id": 23, "name": "Susan", "address": "One way 98"},
                { "_id": 24, "name": "Vicky", "address": "Yellow Garden 2"},
                { "_id": 25, "name": "Ben", "address": "Park Lane 38"},
                { "_id": 26, "name": "William", "address": "Central st 954"},
                { "_id": 27, "name": "Chuck", "address": "Main Road 989"},
                { "_id": 28, "name": "Viola", "address": "Sideway 1633"}
            ]

dblist = myclient.list_database_names()  # creating object for name of collections.

print(myclient.list_database_names())    # In MongoDB, a database is not created until it gets content, so if this is your first time creating a database, you should complete the next two chapters (create collection and create document) before you check if the database exists!

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

for x in mycol.find():
  print(x)

if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("The database doesnt exists.")

# myquery = { "address": "Park Lane 38" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# myquery = { "address": { "$gt": "S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#address starts with S:
# myquery = { "address": { "$regex": "^S" } }
# mycol.delete_one(myquery)
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# mydoc = mycol.find().sort("name")
# mydoc = mycol.find().sort("name", 1)

# mydoc = mycol.find().sort("name", -1)


# for x in mydoc:
#   print(x)


# myquery = { "address": {"$regex": "^S"} }

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

# x = mycol.delete_many({})

# print(x.deleted_count, " documents deleted.")


# mycol = mydb["customers"]

# mycol.drop()








# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }

# mycol.update_one(myquery, newvalues)

# #print "customers" after the update:
# for x in mycol.find():
#   print(x)


# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }

# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")



# myresult = mycol.find().limit(5)

# #print the result:
# for x in myresult:
#   print(x)
