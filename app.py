from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
import json
from config import key, token
import Trello

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

app = Flask(__name__)
app.config.from_object('flask_config.Config')
"""
get_boards = "https://api.trello.com/1/members/me/boards"


headers = {
    "Accept": "application/json"
}

query = {
    'key': key,
    'token': token
}

all_boards = requests.request(
   "GET",
   get_boards,
   headers=headers,
   params=query
)

board_id = all_boards.json()[0]['id']
print(board_id)
generate_list_string = "https://api.trello.com/1/boards/{}/lists/".format(board_id)


all_lists = requests.request(
   "GET",
   generate_list_string,
   headers=headers,
   params=query
)

lists = all_lists.json()

for list in lists:
    print(list)

#print(json.dumps(json.loads(all_lists.text), sort_keys=True, indent=4, separators=(",", ": ")))

#all_cards_things_to_do = requests.request(
#   "GET",
#   get_cards,
#   headers=headers,
#   params=query
#)


list_id = all_lists.json()[1]['id']
card_to_move = "https://api.trello.com/1/lists/{}/cards/".format(list_id)

print(card_to_move)
move_card = requests.request(
   "PUT",
   card_to_move,
   headers=headers,
   params=query
)

print(generate_list_string)
"""
@app.route('/', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def index():
    if request.method == 'POST':
        NewItem = request.form["NewItem"]
        session.add_item(NewItem)
        return render_template('index.html', items = session.get_items())
    elif request.method == 'PUT':
        SelectedItem = requestform["CompleteTask"]
        session.save_item()
        return render_template('index.html', items = session.get_items())
    else:
        return render_template('index.html', lists = Trello.get_all_cards())

if __name__ == '__main__':
    app.run()
