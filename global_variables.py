import pymongo
# Function name: get_collection
# Purpose: gets a collection in a mongodb database
# Inputs: 
#     db_string: A string with a uri for a port being listened to by mongosh
#     db_name: The name of the database containing the desired collection
#     collection_name: The name of the desired collection
# Outputs: 
#     collection: a mongodb collection named scholarship_info 
def get_collection(db_string, db_name, collection_name):
    client = pymongo.MongoClient(db_string)
    database = client[db_name]
    collection = database[collection_name]
    return collection

#The name of the excel file
EXCEL_FILE_NAME = 'scholarships.xlsx'

#the name of the excel sheet
EXCEL_SHEET_NAME = 'Scholarships'

COLUMNS = ['Name', 'Amount', 'Due date', 'Applications', 'Difficulty']