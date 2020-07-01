import pymongo


class TestMongoDB(object):

    def __init__(self, UrlName, TableName):
        self.UrlName = UrlName
        self.TableName = TableName
        self.moclient = pymongo.MongoClient("mongodb://" + self.UrlName + "")
        self.modb = self.moclient[self.TableName]

        # createCollection

    def select(self, CollectionName, Term, Field):
        # for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
        #     print(x)

        mocol = self.modb[CollectionName]
        # moquery = { "phone": "8618770185021" }
        msg = mocol.find(Term)
        msg_list = []
        for msgindex in msg:
            msg_list.append(msgindex)
            # print(msg_list[0][Field])
            return msg_list[0][Field]

    def insert(self, CollectionName, message):

        collist = self.modb.list_collection_names()
        if CollectionName in collist:

            mocol = self.modb[CollectionName]
            mocol.insert_one(message)
        else:

            mocol = self.modb[CollectionName]
            mocol.insert_one(message)

    def update(self, CollectionName, Term, update_msg):
        # myquery = { "Name": name }
        newvalues = {"$set": update_msg}
        mocol = self.modb[CollectionName]
        mocol.update_one(Term, newvalues)

# if __name__ == "__main__":
#     UrlName = 'localhost:27017/'
#     TableName = 'test_defiex'
#     CollectionName = 'AccountMessage'

#     execute = TestMongoDB(UrlName,TableName)
#     Term = { "phone": "8618770185021" }
#     execute.select(CollectionName,Term,"token")


#     CollectionName = 'General_account'
#     with sql.SqlSave() as executes:
#         msg = executes.selects('Admin_testname')

#     for msg in msg:
#         message = {"Name":msg[0],"Password":msg[1],"Code":msg[2]}
#         execute.insert(CollectionName,message)


# message = {"UrlName":"登录","Url":"/api/187034?do="}
# execute.insert(CollectionName,message)


# 查询所有纪录
# mycol.find()
