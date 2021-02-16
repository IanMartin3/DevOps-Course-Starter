from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json

"""
Required for all Trello API Calls
"""
headers = {
    "Accept": "application/json"
}

trello_params = {
    'key': os.getenv('TRELLO_KEY'),
    'token': os.getenv('TRELLO_TOKEN')
}

"""
Get Trello Board 
"""
get_boards = "https://api.trello.com/1/members/me/boards"

all_boards = requests.request(
   "GET",
   get_boards,
   headers=headers,
   params=trello_params
)

boards = all_boards.json()
board_id = all_boards.json()[0]['id']

"""
Get All Trello Lists 
"""
generate_list_string = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists/"

all_lists = requests.request(
   "GET",
   generate_list_string,
   headers=headers,
   params=trello_params
)

lists = all_lists.json()

list_id = all_lists.json()[0]['id']

def cards_from_things_to_do():
   get_cards_from_things_to_do = f"https://api.trello.com/1/lists/{os.getenv('THINGS_TO_DO_LIST_ID')}/cards/"
   all_cards_from_things_to_do = requests.request(
      "GET",
      get_cards_from_things_to_do,
      headers=headers,
      params=trello_params
   )

   return all_cards_from_things_to_do.json()

def cards_from_doing():
   get_cards_from_doing = f"https://api.trello.com/1/lists/{os.getenv('DOING_LIST_ID')}/cards/"
   all_cards_from_doing = requests.request(
      "GET",
      get_cards_from_doing,
      headers=headers,
      params=trello_params
   )

   return all_cards_from_doing.json()

def cards_from_done():
   get_cards_from_done = f"https://api.trello.com/1/lists/{os.getenv('DONE_LIST_ID')}/cards/"
   all_cards_from_done = requests.request(
      "GET",
      get_cards_from_done,
      headers=headers,
      params=trello_params
   )

   return all_cards_from_done.json()

post_things_to_do = f"https://api.trello.com/1/lists/{os.getenv('THINGS_TO_DO_LIST_ID')}/cards/"

post_doing = f"https://api.trello.com/1/lists/{os.getenv('DOING_LIST_ID')}/cards/"

post_done = f"https://api.trello.com/1/lists/{os.getenv('DONE_LIST_ID')}/cards/"


"""
Add Cards to Lists on Trello Board 
"""
def add_thing_to_do(): 
    NewThingToDo = request.form['NewThingToDo']
    requests.post(post_things_to_do, params={**trello_params, 'name': NewThingToDo})
    return redirect(url_for('index'))

def add_doing(): 
    NewDoingTask = request.form['NewDoingTask']
    requests.post(post_doing, params={**trello_params, 'name': NewDoingTask})
    return redirect(url_for('index'))

def add_done(): 
    NewDoneTask = request.form['NewDoneTask']
    requests.post(post_done, params={**trello_params, 'name': NewDoneTask})
    return redirect(url_for('index'))