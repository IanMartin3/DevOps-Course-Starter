from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json
import moment
from datetime import datetime

#Required for all Trello API Calls
headers = {
    "Accept": "application/json"
}

trello_params = {
    'key': os.getenv('TRELLO_KEY'),
    'token': os.getenv('TRELLO_TOKEN')
}

#Get Trello Board
def boards():
   get_all_boards = "https://api.trello.com/1/members/me/boards"
   all_boards = requests.request(
      "GET",
      get_all_boards,
      headers=headers,
      params=trello_params
   )

   return all_boards.json()

#Get All Lists 
def lists_on_this_board():
   get_all_lists = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists/"
   all_lists = requests.request(
      "GET",
      get_all_lists,
      headers=headers,
      params=trello_params
   )

   return all_lists.json()

#Get All Cards 
def cards_on_this_board():
   get_all_cards = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards/"
   all_cards = requests.request(
      "GET",
      get_all_cards,
      headers=headers,
      params=trello_params
   )

   return all_cards.json()

#Variables for adding cards to lists
post_things_to_do = f"https://api.trello.com/1/lists/{os.getenv('THINGS_TO_DO_LIST_ID')}/cards/"
post_doing = f"https://api.trello.com/1/lists/{os.getenv('DOING_LIST_ID')}/cards/"
post_done = f"https://api.trello.com/1/lists/{os.getenv('DONE_LIST_ID')}/cards/"

#Variables for list ids 
todoid = f"{os.getenv('THINGS_TO_DO_LIST_ID')}"
doingid = f"{os.getenv('DOING_LIST_ID')}"
doneid = f"{os.getenv('DONE_LIST_ID')}"

#Add Cards to Lists on Trello Board 
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

def move_card_to_todo(id):
   url = f"https://api.trello.com/1/cards/{id}"
   requests.put(url, params={**trello_params, 'idList': {os.getenv('THINGS_TO_DO_LIST_ID')}})

def start_card(id):
   url = f"https://api.trello.com/1/cards/{id}"
   requests.put(url, params={**trello_params, 'idList': {os.getenv('DOING_LIST_ID')}})

def complete_card(id):
   url = f"https://api.trello.com/1/cards/{id}"
   requests.put(url, params={**trello_params, 'idList': {os.getenv('DONE_LIST_ID')}})
