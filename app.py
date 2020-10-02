from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
import json
from config import key, token

app = Flask(__name__)
app.config.from_object('flask_config.Config')

get_board = "https://api.trello.com/1/members/me/boards"

headers = {
    "Accept": "application/json"
}

query = {
    'key': key,
    'token': token
}

all_boards = requests.request(
   "GET",
   get_board,
   headers=headers,
   params=query
)

#get_cards = "https://api.trello.com/1/members/me/cards/{all_boards.id}"

#all_cards = requests.request(
#   "GET",
#   get_cards,
#   headers=headers,
#   params=query
#)

print(json.dumps(json.loads(all_boards.text), sort_keys=True, indent=4, separators=(",", ": ")))
#print(json.dumps(json.loads(all_cards.text), sort_keys=True, indent=4, separators=(",", ": ")))

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
        return render_template('index.html', items = session.get_items())

if __name__ == '__main__':
    app.run()
