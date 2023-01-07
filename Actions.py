from os import system

def clear():    # clears terminal!! :D
    for i in range(4):
        print("\n")
    #system("clear")

def int_txtBox():      # integer text box method just gives us a clean consistant integer text box!!! :D
    value = input(">>> ")
    if value == '': 
        input("Uh, oh\nPlease type an integer\nPress [Enter] to try again >>> ")
        int_txtBox()
    try: value = int(value)
    except: 
        ValueError
        input("Uh, oh\nPlease type an integer\nPress [Enter] to try again >>> ")
        clear()
        int_txtBox()   
             
    return value

def str_txtBox():      # string text box like int_txt_box but for strings and gives us a clean consistant text box!! :D
    value = input(">>> ")
    try: value = value.lower()
    except: ValueError
    return str(value)

def calculateValue(shares):
    value = 0
    for i in range(len(shares)):
        value += shares[i].owned * shares[i].bid
    return value # returns the value of all of your shares combined