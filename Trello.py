from flask import session
import requests
from config import key, token

_DEFAULT_ITEMS = [
    { 'id': 1, 'name': 'Not Started', 'idBoard': 'List saved todo items' },
    { 'id': 2, 'name': 'Not Started', 'idBoard': 'Allow new items to be added' }
]

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

list_id = all_lists.json()[1]['id']
card_to_move = "https://api.trello.com/1/lists/{}/cards/".format(list_id)
"""
print(card_to_move)
move_card = requests.request(
   "PUT",
   card_to_move,
   headers=headers,
   params=query
)
"""
def get_all_cards():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return lists



    

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

