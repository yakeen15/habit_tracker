from datetime import datetime, timedelta

class Habit:
    def __init__(self, name):
        self.name = name
        self.days = []

    def check(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.days:
            self.days.append(today)
