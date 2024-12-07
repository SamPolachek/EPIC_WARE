from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.before_request
def initialize_food_items():
    # Check if 'food_items' exists in the session; if not, initialize it
    if 'food_items' not in session:
        session['food_items'] = [
            {"name": "Food 1", "expiration": "2024-10-01", "quantity": 6},
            {"name": "Food 2", "expiration": "2024-11-15", "quantity": 12},
            {"name": "Food 3", "expiration": "2024-12-20", "quantity": 8}
        ]


@app.route('/')
def index():
    # Always get food_items from session before rendering
    food_items = session['food_items']
    return render_template('index.html', food_items=food_items)


@app.route('/create')
def create():
    return render_template('create.html')

# Change this later to work with /edit/item
@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/increase/<int:item_index>', methods=['POST'])
def increase(item_index):
    # Ensure food_items exists in session
    food_items = session.get('food_items', [])
    
    if 0 <= item_index < len(food_items):
        food_items[item_index]['quantity'] += 1  # Increment the quantity
        session['food_items'] = food_items  # Update session data
    
    return redirect(url_for('index'))

@app.route('/decrease/<int:item_index>', methods=['POST'])
def decrease(item_index):
    # Ensure food_items exists in session
    food_items = session.get('food_items', [])
    
    if 0 <= item_index < len(food_items) and food_items[item_index]['quantity'] > 0:
        food_items[item_index]['quantity'] -= 1  # Decrement the quantity
        session['food_items'] = food_items  # Update session data
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
