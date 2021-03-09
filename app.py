from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import trello
import os
import moment
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        all_my_boards = trello.boards(),
        all_my_lists = trello.lists_on_this_board(),
        all_my_cards = trello.cards_on_this_board(),
        todo_id = trello.todoid,
        doing_id = trello.doingid,
        done_id = trello.doneid
    )

@app.route('/add_thing_to_do/', methods=['POST'])
def add_thing_to_do():
    return trello.add_thing_to_do()

@app.route('/add_doing/', methods=['POST'])
def add_doing():
    return trello.add_doing()

@app.route('/add_done/', methods=['POST'])
def add_done():
    return trello.add_done() 

@app.route('/move_card_to_to_do/<id>')
def move_card_to_to_do(id):
    trello.move_card_to_todo(id)
    return redirect(url_for('index'))

@app.route('/move_card_to_doing/<id>')
def move_card_to_doing(id):
    trello.start_card(id)
    return redirect(url_for('index'))

@app.route('/move_card_to_done/<id>')
def move_card_to_done(id):
    trello.complete_card(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)