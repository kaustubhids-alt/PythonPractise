class Train:
    def __init__(self, name, ticket, seats):
        self.name = name
        self.ticket = ticket
        self.seats = seats

    def get_status(self):
        print(f"The train {self.name} has {self.seats} seats.")

    def get_ticket_info(self):
        print(f"The ticket of train {self.name} is {self.ticket}.")

   
train = Train("Vande Bharat", 1500, 200)

train.get_status()
train.get_ticket_info()