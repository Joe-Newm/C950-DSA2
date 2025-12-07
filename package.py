class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.loadingTime = 0 
        self.deliveryTime = 0

    def __str__(self):
        return f'id: {self.id}\naddress: {self.address}\ncity: {self.city}\nstate: {self.state}\nzip: {self.zip}\ndeadline: {self.deadline}\n weight: {self.weight}\nnotes: {self.notes}\nloading Time: {self.loadingTime}\ndeliveryTime: {self.loadingTime}\n\n'

    def __repr__(self):
        return f'id: {self.id}\naddress: {self.address}\ncity: {self.city}\nstate: {self.state}\nzip: {self.zip}\ndeadline: {self.deadline}\nweight: {self.weight}\nnotes: {self.notes}\nloading Time: {self.loadingTime}\ndeliveryTime: {self.loadingTime}\n\n'