class Package:
    def __init__(self, id, city, state, zip, deadline, weight, notes, loadingTime, deliveryTime):
        self.id = id
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.loadingTime = loadingTime
        self.deliveryTime = deliveryTime

    def __str__(self):
        return print(f'id: {self.id}\ncity: {self.city}\nstate: {self.state}\nzip: {self.zip}\ndeadline: {self.deadline}\n weight: {self.weight}\nloading Time: {self.loadingTime}\ndeliveryTime: {self.loadingTime}\n')

    def __repr__(self):
        return print(f'id: {self.id}\ncity: {self.city}\nstate: {self.state}\nzip: {self.zip}\ndeadline: {self.deadline}\n weight: {self.weight}\nloading Time: {self.loadingTime}\ndeliveryTime: {self.loadingTime}\n')