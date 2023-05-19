########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = #FillinMissingCode
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    newString += #FillinMissingCode (assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2
#check to add the chars at the end
#FillinMissingCode

print (newString)

########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = #FillinMissingCode
for letter in myName:
    print(#FillinMissingCode)
        

########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = #FillinMissingCode
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
     #FillinMissingCode - check if the word has more than one char

    word = word[1:] + firstChar + pigLatinKey
    print( #FillinMissingCode)
        
########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = #FillinMissingCode
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
         #FillinMissingCode - check if the char is vowel or not
        
     

    word = #FillinMissingCode  
    print( #FillinMissingCode)
