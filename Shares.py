from random import shuffle
from time import sleep
class Shares:   # shares class is only a blueprint!
    def __init__(self, bid, offer, volatility, name, rname):
        self.bid = bid
        self.offer = offer
        self.volatility = volatility
        self.name = name
        self.rname = rname
        # these are my variables ready for use! :D

        # no methods for Shares :(
    def getBid(self):
        return self.bid

    def getOffer(self):
        return self.offer

    def priceChange(self, l, shares):
        difference = self.offer - self.bid
        price_change = (self.bid * self.volatility) / 100
        up_or_down = [-1, 1]
        shuffle(up_or_down) # random!!
        validator = self.bid + (price_change * up_or_down[0])
        if int(validator) - difference <= 0: self.bustShares(l, shares)
        self.bid = self.bid + (price_change * up_or_down[0])
        self.offer = self.bid + difference
    
    def bustShares(self, l, shares): 
        shares[l].name = f"{shares[l].name} files for bankruptcy"
        shares[l].offer = 0
        del shares[l]

    
    
    

        
        

    
        

