import pendulum

class my_card:
    def __init__(self, id, name, list, due_date, modified_date):
        self.id = id
        self.name = name
        self.list = list
        self.due_date = due_date
        self.modified_date = modified_date