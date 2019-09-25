from pymongo import MongoClient
import json
client = MongoClient('localhost', 27017)

db = client['pymongo_test']
cursor = db.pymongo_test


posts = db.posts
# post_data = {
#     'Name': 'Milk',
#     'Quantity': '1',
#     'Expiration Date': '4/03/20'
# }
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))
#
# post_1 = {
#     'title': 'PyMongo!!!',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# post_2 = {
#     'title': 'Virtual Environments',
#     'content': 'Use virtual environments, you guys',
#     'author': 'Scott'
# }
# post_3 = {
#     'title': 'Learning Python',
#     'content': 'Learn Python, it is easy',
#     'author': 'Bill'
# }
# new_result = posts.insert_many([post_1, post_2, post_3])
# print('Multiple posts: {0}'.format(new_result.inserted_ids))
#d = dict((db, [collection for collection in client[db].list_collection_names()]) for db in client.list_database_names())

#print(json.dumps(d))

for document in posts.find():
    print(document)