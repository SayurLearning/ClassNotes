

Flowers = {
    'lotus':
        { "cost": 12,
          "stock": 35,
          "profit": 3
          },
    'rose': {"cost": 16, "stock": 30, "profit": 4},
    'lily': {"cost": 19, "stock": 27, "profit": 5}}
#print(Flowers['lotus'])
#Jasmine, 20, 50, 6


print (Flowers['lily']['cost'])


Flowers['rose']['cost'] = 20
Flowers['rose']['stock'] = 50
Flowers['rose']['profit'] = 6

for key in Flowers :
    print (key, Flowers[key]['cost'] )

# Count the number of each chars in a string. Use Dictionary. 
# Print the chars and its num of occurrence in the same order as it appears in the string
#we attack at dawn
#output -  w2e1a4...