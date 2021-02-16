from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import Trello
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
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
    return Trello.add_thing_to_do()

@app.route('/add_doing/', methods=['POST'])
def add_doing():
    return Trello.add_doing()

@app.route('/add_done/', methods=['POST'])
def add_done():
    return Trello.add_done() 

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