import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name):
        self.name = name
        self.days = []
        self.max_streak = 0
        self.current_streak = 0

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
    
    def streak(self):
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in self.days]
        max_count = self.max_streak
        if self.days:
            counter = 1
            if max_count<1:
                max_count=1
        else:
            counter = 0
        for i in range(1, len(self.days)):
            if dates[i] - dates[i-1] == timedelta(days=1):
                counter = counter+1
                max_count = max(max_count, counter)
            else:
                if self.days:
                    counter = 1
                else:
                    counter = 0
        self.max_streak = max_count
        self.current_streak = counter


class Tracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name):
        stat = 0
        if name not in self.habits:
            self.habits[name] = Habit(name)
            stat = 1
        return stat

    def remove_habit(self, name):
        stat = 0
        if name in self.habits:
            del self.habits[name]
            stat = 1
        return stat

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

    def completion(self, date = datetime.now().strftime("%Y-%m-%d")):
        msg = f"{date}\n"
        for name, habit in self.habits.items():
            stat = "not done"
            if habit.status(date):
                stat = "done"
            msg = msg + f"{name}\t:\t{stat}\n"
        return msg
    
    def show_streaks(self):
        msg = f"Streak data\n"
        for name, habit in self.habits.items():
            habit.streak()
            msg = msg+f"{name}\tCurrent Streak:\t{habit.current_streak}\tMax Streak:\t{habit.max_streak}\n"
        return msg
