from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dummy data with quantity for each food item
    a = ["Food 1", "2024-10-01", 6]
    food_items = [
        {"name": a[0], "expiration": a[1], "quantity": a[2]},
        {"name": "Food 2", "expiration": "2024-11-15", "quantity": 12},
        {"name": "Food 3", "expiration": "2024-12-20", "quantity": 8}
    ]
    return render_template('index.html', food_items=food_items)

@app.route('/create')
def create():
    return render_template('create.html')

# Change this later to work with /edit/item
@app.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)
