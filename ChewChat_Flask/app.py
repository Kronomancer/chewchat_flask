from flask import Flask, render_template
from classes.comment import Comment, Thread
from classes.food_item import FoodItem
from classes.page import Page, City, Restaurant
from classes.user import User
from functions.construct_from_file import constructFromFile

app = Flask(__name__)
# http://127.0.0.1:5000
# python3 /Users/alan/Documents/Calhacks-10.0/app.py

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)