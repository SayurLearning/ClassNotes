######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input#FillinMissingCode)
noOfEntries = int (input("How many rows do you want to print"))

for i in range (1,#FillinMissingCode):
    print (i , "*" , multiplicationNumber , " = ", #FillinMissingCode))
           
######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.

######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $
n = int(input("Enter the number of rows: "))

#print the top triangle
for i in range(n):
    print(" "*(n-i-1) + "# "*(i+1)) 
#FillinMissingCode for drawing the bottom triangle

