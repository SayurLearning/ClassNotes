#remove all  a from the input string. remove one letter at a time
# eg input Bash . output  'Bsh' not 'B sh'

word =  input("Enter a word ") 
output = ''

for i in word :
    if (i != 'a') :
        output += i

print (output)
