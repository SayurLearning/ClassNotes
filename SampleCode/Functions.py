print("Welcome to Shop")
print("vadi 30")
print("soda 20")
print("sandwich 100")
vadai_qty = int(input("Enter the quantity of vadai bought: "))

soda_qty = int(input("Enter the quantity of soda bought: "))

sandwich_qty = int(input("Enter the quantity of sandwich bought: "))

vadai_cost = 30
soda_cost = 20
sandwich_cost = 100
total_cost = vadai_qty * vadai_cost + soda_qty * soda_cost + sandwich_qty * sandwich_cost
print(" Your total cost is:",total_cost)

'''
if (condition is True):
    Execute this line 
else 
    Execute this line
'''

for i in range (5):
    print (i)
 

print ("End ")

'''
#Loop
askforMoney = True #Boolean variable
while (askforMoney): 
    amount_paid = float(input("Enter the amount paid: "))
    if (amount_paid==total_cost) : 
        print("Thank You")
        askforMoney = False
    elif (amount_paid > total_cost) :
        change = amount_paid - total_cost
        print("Change amount:", change)
        askforMoney = False
    else :
        remaing = total_cost - amount_paid
        print("Remaing amount:", remaing)
        total_cost = remaing

print ("Program end")

'''



'''
    remaingamount_paid= float(input("Enter the amount paid: "))
    if (remaingamount_paid==remaing) :
        print("Thank You")
    elif (remaingamount_paid > remaing) :
        change = remaingamount_paid - remaing
        print("Change amount:", change)
    else :
        remaing = remaing - remaingamount_paid
        print("Remaing amount:", remaing)
'''