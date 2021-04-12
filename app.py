from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import trello
from view_model import ViewModel

def create_app():
    app = Flask(__name__)
    trello_api = trello.TrelloAPI()
    card_call = trello.card_service()
    @app.route('/', methods=['GET'])
    def index():
        items = card_call.card_details(trello_api.get_all_cards_on_this_board())
        item_view_model = ViewModel(items)
        return render_template(
            'index.html',
            all_my_boards = trello.boards(),
            view_model=item_view_model
        )

    @app.route('/add_thing_to_do/', methods=['POST'])
    def add_thing_to_do():
        return trello.TrelloAPI.add_thing_to_do()

    @app.route('/add_doing/', methods=['POST'])
    def add_doing():
        return trello.TrelloAPI.add_doing()

    @app.route('/add_done/', methods=['POST'])
    def add_done():
        return trello.TrelloAPI.add_done() 

    @app.route('/move_card_to_to_do/<id>')
    def move_card_to_to_do(id):
        trello.TrelloAPI.move_card_to_todo(id)
        return redirect(url_for('index'))

    @app.route('/move_card_to_doing/<id>')
    def move_card_to_doing(id):
        trello.TrelloAPI.start_card(id)
        return redirect(url_for('index'))

    @app.route('/move_card_to_done/<id>')
    def move_card_to_done(id):
        trello.TrelloAPI.complete_card(id)
        return redirect(url_for('index'))
    
    return app

app = create_app()