class DataCollector:
    def __init__(self, user_name, computer_name, index_selected, comment, date_time):
        self.user_name = user_name
        self.computer_name = computer_name
        self.index_selected = index_selected
        self.comment = comment
        self.date_time = date_time

    def __str__(self):
        return f"User: {self.user_name}, Computer: {self.computer_name}, Option: {self.index_selected}, Comment: {self.comment}, Date/Time: {self.date_time}"