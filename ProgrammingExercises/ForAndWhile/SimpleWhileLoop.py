######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import #FillinMissingCode
computerNo = random.randint(3, 9)

attempt = 0
while(True):
    userNo = int (#FillinMissingCode)
    #FillinMissingCode
    attempt +=1

print ("User guessed the number in ", attempt, "attempts")

########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, greenBags = 100, 200
totalSales , totalBagsSold = 0

while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    #FillinMissingCode
    
    #calculate total cost for the bags
     #FillinMissingCode
    totalSales +=  #FillinMissingCode
    #increment no of bags sold
    totalBagsSold +=  #FillinMissingCode

print ( #FillinMissingCode)   
