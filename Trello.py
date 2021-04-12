from flask import request, redirect, url_for
import requests
import os
from datetime import datetime
from card import my_card
import pendulum

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

#For module 3
class TrelloAPI:

    def __init__(self):
        self.trello_key = os.getenv('TRELLO_KEY'),
        self.trello_token = os.getenv('TRELLO_TOKEN')
        self.trello_board_id = os.getenv('TRELLO_BOARD_ID')
        self.trello_todo_list_id = os.getenv('THINGS_TO_DO_LIST_ID')
        self.trello_doing_list_id = os.getenv('DOING_LIST_ID')
        self.trello_done_list_id = os.getenv('DONE_LIST_ID')

    #Get All Boards
    def get_all_boards(self):
        url = "https://api.trello.com/1/members/me/boards"
        response = requests.get(url, params={"key": self.trello_key, "token": self.trello_token}).json()
        return response

    #Get All Lists
    def get_all_lists_on_this_board(self):
        url = f"https://api.trello.com/1/boards/{self.trello_board_id}/lists/"
        response = requests.get(url, params={"key": self.trello_key, "token": self.trello_token}).json()
        return response

    #Get All Cards 
    def get_all_cards_on_this_board(self):
        url = f"https://api.trello.com/1/boards/{self.trello_board_id}/cards/"
        response = requests.get(url, params={"key": self.trello_key, "token": self.trello_token}).json()
        return response

    #Add Cards to Lists on Trello Board 
    def add_thing_to_do(): 
        post_things_to_do = f"https://api.trello.com/1/lists/{os.getenv('THINGS_TO_DO_LIST_ID')}/cards/"
        NewThingToDo = request.form['NewThingToDo']
        requests.post(post_things_to_do, params={**trello_params, 'name': NewThingToDo})
        return redirect(url_for('index'))

    def add_doing():
        post_doing = f"https://api.trello.com/1/lists/{os.getenv('DOING_LIST_ID')}/cards/" 
        NewDoingTask = request.form['NewDoingTask']
        requests.post(post_doing, params={**trello_params, 'name': NewDoingTask})
        return redirect(url_for('index'))

    def add_done():
        post_done = f"https://api.trello.com/1/lists/{os.getenv('DONE_LIST_ID')}/cards/"
        NewDoneTask = request.form['NewDoneTask']
        requests.post(post_done, params={**trello_params, 'name': NewDoneTask})
        return redirect(url_for('index'))

    #Move Cards to between Lists on Trello Board
    def move_card_to_todo(id):
        url = f"https://api.trello.com/1/cards/{id}"
        requests.put(url, params={**trello_params, 'idList': {os.getenv('THINGS_TO_DO_LIST_ID')}})

    def start_card(id):
        url = f"https://api.trello.com/1/cards/{id}"
        requests.put(url, params={**trello_params, 'idList': {os.getenv('DOING_LIST_ID')}})

    def complete_card(id):
        url = f"https://api.trello.com/1/cards/{id}"
        requests.put(url, params={**trello_params, 'idList': {os.getenv('DONE_LIST_ID')}})



       
class CardService:
    def __init__(self):
      self.todo_list_id = os.getenv('todo_list_id')
      self.doing_list_id = os.getenv('doing_list_id')
      self.trello_todo_list_id = os.getenv('THINGS_TO_DO_LIST_ID')
      self.trello_doing_list_id = os.getenv('DOING_LIST_ID')
      self.trello_done_list_id = os.getenv('DONE_LIST_ID')

    def card_details(self, data):
        trello_cards = []
        for item in data:
            card_id = item['id']
            card_name = item['name']
            if item['idList'] == self.trello_todo_list_id:
                card_status = "ToDo"
            elif item['idList'] == self.trello_doing_list_id:
                card_status = "Doing"
            elif item['idList'] == self.trello_done_list_id:
                card_status = "Done"
            card_due_date = item['due']
            card_modified_date = item['dateLastActivity']                    
            card = my_card(card_id, card_name, card_status, card_due_date, card_modified_date)            
            trello_cards.append(card)            
        return trello_cards
