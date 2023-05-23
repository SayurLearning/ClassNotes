############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ):
#convert movies into a List
#FillinMissingCode

commonMoviewCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ( )#FillinMissingCode)
    #Check if this movie is in the movie list
    #FillinMissingCode

    #if present, 
    commonMoviewCount ++
    #check if we reached the max
    if(commmonMovieCount >= 3):
        break;
    else
        print ("Try again")

print () #FillinMissingCode - list all the common movies


############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed

for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    #FillinMissingCode
    currentMonthSalary = #FillinMissingCode
    print (f"This month's salary before additional bonus {currentMonthSalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #calculate the new salary
    currentMonthSalary =   #FillinMissingCode
    print(f}This month's salary after additional bonus {currentMonthSalary})
    previousMonthSalary = currentMonthSalary #Why are we doing this?

 
     