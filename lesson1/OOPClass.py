class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)

sue = Worker('Sue Jones', 60000)
bob = Worker('Bob Smith', 50000)
print(bob.lastName())
sue.giveRaise(.10)
print(sue.pay)
