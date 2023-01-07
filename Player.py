from Portfolio import Portfolio

class Player:
    def __init__(self, name, balance, shares):
        self.name = name
        self.balance = balance
        self.portfolio = Portfolio(shares)
    
    def getBalance(self):   return self.balance