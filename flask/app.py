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

if __name__ == '__main__':
    app.run(debug=True)
