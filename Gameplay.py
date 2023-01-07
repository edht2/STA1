#from datetime import datetime
from Actions import clear, str_txtBox
from Shares import Shares
from Player import Player
from Portfolio import Portfolio


class Gameplay: 
    def __init__(self):
        # Name           |  Bid  |   Offer    |vol|       Name      |Refrence Name|
        self.mvidia    = Shares(100.56,   102.80,   2,   'Mvidia Inc.    ', 'mvidia'    )
        self.tezla     = Shares(235.40,   238.70,   5,   'Tezla Inc.     ', 'tezla'     )
        self.alphabets = Shares(174.30,   181.60,   3,   'Alpherbets Inc.', 'alpherbets')
        self.stop_tb   = Shares(281.20,   284.50,   1,   'Stop TB        ', 'stop tb'   )
        self.apples    = Shares(65.10,    68.40,    75,   'Apples         ', 'apples'    )        
        self.shares = [self.mvidia, self.tezla, self.alphabets, self.stop_tb, self.apples]
        self.player = Player('Alfred', 25000, self.shares) 
        print(self.player.portfolio.name)
        self.display()     

    
    def display(self):
        while True:
            self.currentPrices()
            print("Press [1] to buy, [2] to sell, [P] to open your portfolio, or [Enter] to wait until tomorrow")
            typed = str_txtBox()
            if   typed == "1": 
                self.player.portfolio.transaction_p1("buy")
                self.player.portfolio.transaction_p2(self.player.balance)
                self.player.balance = self.player.portfolio.transaction_p3(self.player.balance)

            elif typed == "2": 
                self.player.portfolio.transaction_p1("sell")
                self.player.portfolio.transaction_p2(self.player.balance)
                self.player.balance = self.player.portfolio.transaction_p3(self.player.balance)

            elif typed == "p": self.player.portfolio.displayPortfolio()
            elif typed == '' : 
                for l in range(len(self.shares)):
                    self.shares[l].priceChange(l, self.shares)
            else: input(f"Unknown command '{typed}'\nPress [Enter] to return >>> ")
  

    def currentPrices(self):   
        clear()
        print(f"---Your Live Stats---\nMoney: ${'{:,.2f}'.format(self.player.balance)}\n")
        for i in range(len(self.shares)): print(f"{self.shares[i].name}    Bid ${'{:,.2f}'.format(self.shares[i].getBid())}    Offer ${'{:,.2f}'.format(self.shares[i].getOffer())}")
        
    



    
    
