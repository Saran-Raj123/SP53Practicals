"""
CP1404/CP5632 Practical - Saranraj Saravanan
Project Class

"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def update(self, percentage, new_priority):
        # Update completion percentage and/or priority
        if percentage:
            self.completion = percentage
        if new_priority:
            self.priority = new_priority
