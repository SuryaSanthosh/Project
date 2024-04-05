from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'myApp'




from flask import Flask, render_template, request, redirect, url_for
# from train import Train

app = Flask(__name__)

trains = []

@app.route('/')
def add_train_form():
    return render_template('addtrain.html')

@app.route('/addtrain', methods=['POST'])
def addtrain():
    train_id = request.form['train_id']
    train_name = request.form['train_name']
    days_of_week = request.form['days_of_week']
    departure_station = request.form['departure_station']
    route = request.form['route']

    train = Train(train_id, train_name, days_of_week, departure_station, route)
    trains.append(train)

    return redirect(url_for('add_train_form'))

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, render_template

app = Flask(__name__)

# Example train object
class Train:
    def __init__(self, train_id, train_name):
        self.train_id = train_id
        self.train_name = train_name
        # Add other train attributes as needed

# Route for displaying train details
@app.route('/train/<train_id>')
def trainview(train_id):
    # Fetch train details from the database or data structure
    # For example:
    # Assuming you have a function to get train details by ID
    train = get_train_by_id(train_id)
    # Here, `train` is an instance of the Train class with all details
    return render_template('trainview.html', train=train)

if __name__ == '__main__':
    app.run(debug=True)
