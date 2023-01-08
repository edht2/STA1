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


    def weightedAverageCalculator(self):
        log = []
        transamount = []
        for l in range(len(self.shares)): 
        
            counter = 0                 
            nt = 0
            count_pre_nt = 0

            for j in range(len(self.transactions)):
                if self.transactions[j][3] == self.shares[l].rname:
                    nt = self.transactions[j][4]

                    if self.transactions[j][2]   == "buy":  
                        count_pre_nt = counter
                        counter += nt

                    elif self.transactions[j][2] == "sell":
                        count_pre_nt = counter
                        counter -= nt

                    if count_pre_nt < 0 and counter >= 0 or count_pre_nt > 0 and counter <= 0: 
                        #print("Toggling between positive and negative or 0")
                        log = []
                        transamount = [counter, self.transactions[j][6]]

                    elif count_pre_nt <= 0 and counter < count_pre_nt or count_pre_nt >= 0 and counter > count_pre_nt:
                        transamount = [self.transactions[j][4], self.transactions[j][6]]
                        log.append(transamount)

                    print('counter', counter, 'count_pre_nt', count_pre_nt)
                    print(transamount)
                    print(log)

    def avPriceCalc(self):
        
        for share in self.shares:
            count = 0
            cmlt = 0  # count minus last transaction
            #print(share.name)
            for tr in self.transactions:
                nt = tr[4]

                if  tr[2] == "buy":  
                    cmlt = count
                    count += nt

                elif tr[2] == "sell":
                    cmlt = count
                    count -= nt
                print(f"cmlt: {cmlt}, count: {count}, nt: {nt}")
    def displayPortfolio(self):
        clear()
        self.weightedAverageCalculator()
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

    
    
        






    
    
        

