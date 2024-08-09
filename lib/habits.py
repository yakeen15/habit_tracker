import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name):
        self.name = name
        self.days = []

    def check(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.days:
            self.days.append(today)

    def uncheck(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today in self.days:
            self.days.remove(today)
    
    def status(self, date = datetime.now().strftime("%Y-%m-%d")): 
        return date in self.days
    

class Tracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name):
        if name not in self.habits:
            self.habits[name] = Habit(name)

    def remove_habit(self, name):
        if name in self.habits:
            del self.habits[name]

    def check(self, name):
        if name in self.habits:
            self.habits[name].check()

    def uncheck(self, name):
        if name in self.habits:
            self.habits[name].uncheck()

    def save_data(self, filename='habit_data.json'):
        data = {name: habits.days for name, habits in self.habits.items()}
        with open(filename, 'w') as file:
            json.dump(data, file, default=str)

    def load_data(self, filename='habit_data.json'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            for name, dates in data.items():
                self.habits[name] = Habit(name)
                self.habits[name].days = dates
        except FileNotFoundError:
            pass

    def habit_data(self, date = datetime.now().strftime("%Y-%m-%d")):
        msg = f"{date}\n"
        for name, habit in self.habits.items():
            stat = "not done"
            if habit.status(date):
                stat = "done"
            msg = msg + f"{name}\t:\t{stat}\n"
        return msg