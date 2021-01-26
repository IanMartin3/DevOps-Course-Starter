from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import Trello
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return render_template(
        'index.html', 
        lists = Trello.lists, 
        boards = Trello.boards,
        cards_from_things_to_do = Trello.cards_from_things_to_do(), 
        cards_from_doing = Trello.cards_from_doing(), 
        cards_from_done = Trello.cards_from_done()
    )

@app.route('/add_thing_to_do/', methods=['POST'])
def add_thing_to_do(): 
    NewThingToDo = request.form['NewThingToDo']
    requests.post(Trello.post_things_to_do, params={**Trello.trello_params, 'name': NewThingToDo})
    return redirect(url_for('index'))

@app.route('/add_doing/', methods=['POST'])
def add_doing(): 
    NewDoingTask = request.form['NewDoingTask']
    requests.post(Trello.post_doing, params={**Trello.trello_params, 'name': NewDoingTask})
    return redirect(url_for('index'))

@app.route('/add_done/', methods=['POST'])
def add_done(): 
    NewDoneTask = request.form['NewDoneTask']
    requests.post(Trello.post_done, params={**Trello.trello_params, 'name': NewDoneTask})
    return redirect(url_for('index'))

@app.route('/move_card_to_to_do/<id>')
def move_card_to_to_do(id):
    card_to_move = f"https://api.trello.com/1/cards/{id}"
    requests.put(card_to_move, headers=Trello.headers, params={**Trello.trello_params, 'idList': {os.getenv('THINGS_TO_DO_LIST_ID')}})
    return redirect(url_for('index'))

@app.route('/move_card_to_doing/<id>')
def move_card_to_doing(id):
    card_to_move = f"https://api.trello.com/1/cards/{id}"
    requests.put(card_to_move, headers=Trello.headers, params={**Trello.trello_params, 'idList': {os.getenv('DOING_LIST_ID')}})
    return redirect(url_for('index'))

@app.route('/move_card_to_done/<id>')
def move_card_to_done(id):
    card_to_move = f"https://api.trello.com/1/cards/{id}"
    requests.put(card_to_move, headers=Trello.headers, params={**Trello.trello_params, 'idList': {os.getenv('DONE_LIST_ID')}})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)