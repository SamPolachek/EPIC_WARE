from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dummy data with quantity for each food item
    food_items = [
        {"name": "Food 1", "expiration": "2024-10-01", "quantity": 5},
        {"name": "Food 2", "expiration": "2024-11-15", "quantity": 12},
        {"name": "Food 3", "expiration": "2024-12-20", "quantity": 8}
    ]
    return render_template('index.html', food_items=food_items)

@app.route('/account')
def account():
    # Dummy data for the account page
    account_info = {
        "username": "johndoe",
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
    return render_template('account.html', account_info=account_info)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

import pymongo
client = pymongo.MongoClient("mongodb+srv://cluster0.tdr34.mongodb.net/")
#access database
db=client["cluster0"]
#access collection
collection= db["account"]
collection= db["items"]

document={"name": "John", "age": 30}
collection.insert_one(document)
#finding a document
#result = collection.find_one({"name":"John"})
#print(result)