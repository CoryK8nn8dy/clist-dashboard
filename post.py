class Post:
    def __init__(self, title, price, date, time):
        self.title = title
        self.price = price
        self.date = date
        self.time = time

    def display(self):
        print('Title:', self.title)
        print('Price:', self.price)
        print('Date:', self.date)
        print('Time:', self.time)
