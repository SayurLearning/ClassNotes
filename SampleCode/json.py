'''
item,  price, type

idli, 25, breakfast
tomato rice, 50, lunch

'''
#.txt, .exe, .bin, .json

menu = [
    {
    "item" : "idli" ,
    "price" :"25",
    "type" : "Breakfast"
},
{
    "item" : "Rice" ,
    "price" :"50",
    "type" : "lunch"
}



]

priceOfRice = menu[1]["price"]
print(priceOfRice)