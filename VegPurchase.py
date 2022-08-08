#This program calculates the how many kg of Onion or Tomato we can buy.
budget = float(input("Please enter the amount you have : ")) #make sure user can give value like 100.50
#print(type(budget)) #used this for debugging
if (budget <= 0): #check for valid budget number
    print("Sorry, you can't buy anything")
else:
    onionprice = 20 #initialize values for the veg
    tomatoprice = 10.5
    amountofonion = budget / onionprice #calcuate onion kgs
    amountoftomato = budget / tomatoprice #calcualte tomato kgs

    #display the results
    print("you can buy ", amountofonion, "kgs of onion")
    print ("or")
    print("you can buy ", amountoftomato, "kgs of tomato")
    