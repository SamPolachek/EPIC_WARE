from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.before_request
def initialize_food_items():
    # Check if 'food_items' exists in the session; if not display the dummy info
    if 'food_items' not in session:
        session['food_items'] = [
            {"name": "Food 1", "expiration": "2024-10-01", "quantity": 6},
            {"name": "Food 2", "expiration": "2024-11-15", "quantity": 12},
            {"name": "Food 3", "expiration": "2024-12-20", "quantity": 8}
        ]


@app.route('/')
def index():
    #get food items previously set
    food_items = session['food_items']
    return render_template('index.html', food_items=food_items)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Ask for input data
        name = request.form['name']
        quantity = int(request.form['quantity'])
        expiration = request.form['expiration']
        location = request.form['location']
        bought_date = request.form['bought_date']
        shelf_stable = 'shelf_stable' in request.form  # Check if checkbox was ticked

        # Create a new data entry
        new_item = {
            "name": name,
            "quantity": quantity,
            "expiration": expiration,
            "location": location,
            "bought_date": bought_date,
            "shelf_stable": shelf_stable
        }

        # Add the new item
        food_items = session['food_items']
        food_items.append(new_item)
        session['food_items'] = food_items  # Update session with new list

        # Redirect back to the index page
        return redirect(url_for('index'))

    return render_template('create.html')

# edit method
@app.route('/edit/<int:item_index>', methods=['GET', 'POST'])
def edit(item_index):
    food_items = session['food_items']
    item = food_items[item_index]

    if request.method == 'POST':
        # Update the food item with the previous input data
        item['name'] = request.form['name']
        item['expiration'] = request.form['expiration']
        item['quantity'] = int(request.form['quantity'])
        session['food_items'] = food_items 
        return redirect(url_for('index'))# go back to home page after

    return render_template('edit.html', item=item, item_index=item_index)
#delete method
@app.route('/delete_item/<int:item_index>', methods=['POST'])
def delete_item(item_index):
    food_items = session['food_items']
    
    if 0 <= item_index < len(food_items):
        # Remove the item 
        del food_items[item_index]
        session['food_items'] = food_items 

    # go back to home page after
    return redirect(url_for('index'))
#increase button method
@app.route('/increase/<int:item_index>', methods=['POST'])
def increase(item_index):
    
    food_items = session.get('food_items', [])
    #make sure there is food to increase
    if 0 <= item_index < len(food_items):
        food_items[item_index]['quantity'] += 1  # Increase by one
        session['food_items'] = food_items 
    # go back to home page after
    return redirect(url_for('index'))
#decrease button
@app.route('/decrease/<int:item_index>', methods=['POST'])
def decrease(item_index):
    
    food_items = session.get('food_items', [])
    
    if 0 <= item_index < len(food_items) and food_items[item_index]['quantity'] > 0:
        food_items[item_index]['quantity'] -= 1  #decrease by one
        session['food_items'] = food_items  
    # go back to home page after
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
