import pprint
from pymongo import MongoClient
from bson import json_util


DB_NAME = 'InsideTheGradebook'
COLLECTION_NAME = 'Students'


# dbname = get_database(DB_NAME)

client = MongoClient("mongodb://127.0.0.1:27017/:27017")

db = client[DB_NAME]

coll1 = db[COLLECTION_NAME] #selecting the coll1 in myDatabase
# for document in coll1.find():
#     print (document)

printer = pprint.PrettyPrinter()

def find_all_students():
     students = coll1.find() 

     for student in students:
         printer.pprint(student)

# find_all_students()

def find_s43():
    tim = coll1.find_one({"student_id": 43, "class_id": 18})
    printer.pprint(tim)

#find_s43()

def count_all_students():
    count = coll1.count_documents(filter={})
    print(count)

#count_all_students()

# def get_score_range(min_score, max_score):
#    # query = coll1.find({"scores": {"score": 87.50309579619501}})

        
#     # query = {"$and": [
#     #     {"score": {"$gte": min_score}},
#     #     {"score": {"$lte": max_score}}
#     # ]}
#     # print("x")
#     # students = coll1.find(query).sort("score") 
#     # print("2")
#     # for studen:
#     #     printer.pprint(student)
#         # print("1")
    
# get_score_range(1.0,100.0)

class_id = 29
#Search students by class 
def search_students_by_class():
    students = coll1.find({"class_id": class_id})

    for itr in students:
        printer.pprint(itr)

#Search students by id
student_id = 45
class_id_sid = 13
#Get list of students in any specific class
def search_students_by_id():
    students = coll1.find({"student_id": student_id, "class_id": class_id_sid})

    for itr in students:
        printer.pprint(itr)

#search_students_by_class()
search_students_by_id() 


