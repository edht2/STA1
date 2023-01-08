from Actions import clear, str_txtBox, int_txtBox
#from Player import Player
from datetime import datetime

class Portfolio:    # portfolio class will caulculate our portfolio, buy and sell! :D
    def __init__(self, shares):
        self.name = "Alfred"
        self.buy_or_sell = ""
        self.chosen_share = ""
        self.volume = 0
        self.transaction = []
        self.transactions = []
        self.shares = shares
        self.index = 0



    
    #def calculateWeightedAverage(self, share):
    #    for i in range(len(self.transactions)):
    #        if share == self.transactions[i][2]:
    #            if self.tarnsactions[i][0] == "buy":
    #                self.transactions[i][]

    def aggregator(self): 
        share_agg = []  
        for h in range(len(self.shares)):
            counter = 0
            for i in range(len(self.transactions)):
                if self.shares[h].rname == self.transactions[i][3]:
                    if self.transactions[i][1] == "buy": counter += self.transactions[i][4]
                    if self.transactions[i][1] == "sell": counter -= self.transactions[i][4]
            if counter != 0: share_agg.append([self.shares[h].name, counter])
            return share_agg


    def avPriceCalc(self):
        
        for share in self.shares:
            count = 0
            cmlt = 0  # count minus last transaction
            trans_log = []
            trans = []
            message = ''
            for tr in self.transactions:
                if tr[3] == share.rname:
                    lt = tr[4]

                    if  tr[2] == "buy":  
                        cmlt = count
                        count += lt

                    elif tr[2] == "sell":
                        cmlt = count
                        count -= lt
                    if cmlt >= 0 and count > cmlt or cmlt <= 0 and count < cmlt: # if square or net long/short and a purchase/sale is made ...
                        trans = [tr[4], tr[6]]
                        trans_log.append(trans)
                        message = 'net long/short and a purchase/sale has been made. ' + tr[3]
                    elif cmlt > 0 and count < 0 or cmlt < 0 and count > 0: # if new transaction reverses the long/short position into a short/long position...
                        trans_log = []
                        trans = [count, tr[6]]
                        trans_log.append(trans)
                        message = 'new transaction reverses the long/short position into a short/long position. ' + tr[3]
                    elif count == 0: # position is 0
                        trans_log = []
                        trans = []
                        message = 'position is 0' + tr[3]
                    else: # player is long / short and a sale/purchase has been made not sufficient to reverse the position. Do nothing
                        message = 'player is long / short and a sale/purchase has been made not sufficient to reverse the position. Do nothing'
                    print(f"{tr[3]}. Trans_log = {trans_log}\nTrans = {trans}\n")
                    print(message)


                

                

    def displayPortfolio(self):
        clear()
        self.avPriceCalc()
        self.aggregator()
        for i in range(len(self.transactions)):
            if self.transactions[i][2] ==  "buy": bs = "+"
            elif self.transactions[i][2] == "sell": bs = "-"
            print(f"\n{i + 1}. {self.transactions[i][3]} {bs}{self.transactions[i][4]} each costing ${'{:,.2f}'.format(self.transactions[i][0])} totaling ${'{:,.2f}'.format(self.transactions[i][6])} at {self.transactions[i][1]}")        
        input("Press [Enter] to return >>> ")     
            
            
            
    def transaction_p1(self, buy_or_sell): # method 'transaction_p1' is the first part of the transaction
        clear()
        self.buy_or_sell = buy_or_sell
        print(f"What share do you want to {self.buy_or_sell}?\n-----------------------------")
        for j in range(len(self.shares)): print(f"- {self.shares[j].rname}")
        chosen_share = str_txtBox() # Opens a txt box
        self.chosen_share = chosen_share
        miss_counter = 0
        for i in range(len(self.shares)):
            self.index = i
            if self.chosen_share == self.shares[self.index].rname: # validator!              
                #self.transaction_p2(balance)  
                break # stops loop
            else: 
                clear()    
                miss_counter += 1 
                if miss_counter >= len(self.shares):        
                    input(f"Hmmm {self.chosen_share} doesn't exist\nPress [Enter] to return >>> ")     
                    self.transaction_p1(buy_or_sell)
        
    


    def transaction_p2(self, balance):
        clear()
        print(f"How many {self.shares[self.index].rname} share(s) do you want to {self.buy_or_sell}?")
        volume = int_txtBox()
        self.volume = volume
        if self.buy_or_sell == "buy":
            if self.volume * self.shares[self.index].offer > balance:
                input("You cannot afford that!\nPress [Enter] to return >>> ")
                self.transaction_p2(balance)
    

    def transaction_p3(self, balance):
        clear()
        
        if self.buy_or_sell == "buy":  
            price = int(self.volume * self.shares[self.index].offer)
            balance -= price 
            self.transaction.append(self.shares[self.index].offer)
            
        elif self.buy_or_sell == "sell": 
            price = int(self.volume * self.shares[self.index].bid)    
            balance += price  
            self.transaction.append(self.shares[self.index].bid)
      
        self.transaction.append(datetime.now())
        self.transaction.append(self.buy_or_sell)
        self.transaction.append(self.chosen_share)
        self.transaction.append(self.volume)
        self.transaction.append(balance)
        self.transaction.append(price)
        
        

        self.transactions.append(self.transaction) # tansactions!!
        self.transaction = []
        return balance

    
    
        






    
    
        

