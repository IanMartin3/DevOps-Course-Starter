from card import my_card
from datetime import datetime 
import pendulum

class ViewModel:
    def __init__(self, items):
        self.items = items

    def items(self):
        return self.items

    def todo_items(self):
        todo_items = []
        for item in self.items:
            if item.list == "ToDo":
                old_modified_date = pendulum.parse(str(item.modified_date)).format('DD/MM/YYYY') 
                modified_date = old_modified_date
                todo_items.append(item)
        return todo_items

    def doing_items(self):
        doing_items = []
        for item in self.items:
            if item.list == "Doing":
                doing_items.append(item)
        return doing_items

    def done_items(self):
        done_items = []
        for item in self.items:
            if item.list == "Done":
                done_items.append(item)
        return done_items