############## Problem  1 #################### 
#Ask first friend the colors they list. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.

############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58
#
nameList = []
ageList = []
#FillinMissingCode for other data
noOfPeople = int (input("How many people in the family"))
for member in range (1, noOfPeople + 1):
    details = input(f"Enter the details of member {member} Name, age, height, weight")
    #FillinMissingCode Split the input string and add it to the lists

#print the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") #learn about \t
for index, member in enumerate(nameList): #Learn how enumerate works
    print( f"{member}\t\t FillinMissingCode to print the details from other lists")