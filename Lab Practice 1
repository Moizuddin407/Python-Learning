# Lab 1
def q1():
    # Q1
    print("Enter Length of Rectangle:")
    l=int(input())
    print("Enter Width of Rectangle:")
    w=int(input())
    a=l*w
    print("Area is:\n",a)

def q2():
    # Q2
    print("Enter marks for Maths:")
    maths=int(input())
    print("Enter marks for Science:")
    science=int(input())
    print("Enter marks for English:")
    Eng=int(input())
    print("Enter marks for Urdu:")
    Urdu=int(input())
    Average=float(((Eng+Urdu+science+maths)/400)*100)
    print(f"Your Consolidated Average is {Average}")

def q7():
    salestax=0.16
    print("Enter number of items:")
    n=int(input())
    Items=[]
    prices=[]
    disc=[]
    for i in range(0,n):
        print("Enter item name:")
        item=input()
        Items.append(item)
        print("Enter item price:")
        price=float(input())
        prices.append(price)
    
    print("Enter item name to buy:")
    buyitem=input()
    for i in range(len(Items)):
        if buyitem == Items[i]:
            priceitem = prices[i]
            print(f"Item:{buyitem}\nPrice:{priceitem}\nTax:{priceitem * salestax}\nTotal price:{priceitem + (priceitem * salestax)}")


def q9baladd(balance,amount):
    balance=balance+amount
    return balance

def q9balsub(balance,amount):
    balance=balance-amount
    return balance

def q9():

    print("Enter starting balance:")
    startbal=float(input())
    baldisp=startbal
    x=False
    while x!=True:
        print("Enter '1' for deposit\nEnter '2' for widthdraw\nEnter '3' for Exit")
        choice=int(input())
        match choice:
            case 1:
                print("Enter amount for deposit\n:")
                amount=float(input())
                startbal=q9baladd(startbal,amount)
                
                print(f"Starting Balance:{baldisp}\nDeposit amount{amount}\nCurrent Balance{startbal}")
            case 2:
                print("Enter amount to widthdraw\n:")
                amount=float(input())
                startbal=q9balsub(startbal,amount)
                
                print(f"Starting Balance:{baldisp}\nDeposit amount{amount}\nCurrent Balance{startbal}")
            case 3:
                x=True
            case _:
                print("Invalid Option. Please choose again!\n")

def q11_50unit(unit):
    return unit*0.5
def q11_150unit():
    return unit*0.75
def q1_250unit():
    return unit*1.2
def q1_250aboveunit():
    return unit*1.5      
def q11():
    print("Enter units used:\n")
    unit=int(input())
    if unit<0:
        print("Error! ! !")
    if unit<=50:
        q11_50unit(unit)
    elif unit >50 and unit <= 150:
        q11_150unit(unit)
    elif unit > 150 and unit <=250:
        q11_250unit(unit)
    else:
        q11_250aboveunit(unit)
        
        
def q15(n):
    listx=[]
    for i in range(1,n+1):
        listx.append(i*i)
    print(listx)
q15(5)