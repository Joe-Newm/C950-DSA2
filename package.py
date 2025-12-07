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
        return f'id: {self.id} address: {self.address} city: {self.city} state: {self.state} zip: {self.zip} deadline: {self.deadline} weight: {self.weight} notes: {self.notes} loading Time: {self.loadingTime} deliveryTime: {self.loadingTime}\n'

    def __repr__(self):
        return f'id: {self.id} address: {self.address} city: {self.city} state: {self.state} zip: {self.zip} deadline: {self.deadline} weight: {self.weight} notes: {self.notes} loading Time: {self.loadingTime} deliveryTime: {self.loadingTime}\n'