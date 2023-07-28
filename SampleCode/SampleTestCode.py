#  "We Attack at Dawn" is input. Output should be 'atwcdekn'
s ='We Attack at Dawn' 
s = s.lower().replace(" ","")

 
print (s)
#create a new string
newS = ''
i = 0
countOfChars = 0
while len(s) > 0 :
    charToCount = s[i]
    cofC = s.count(charToCount)
    newS = newS + charToCount + str(cofC) + ' '
    countOfChars += 1
    #remove all occurance of Char
    s = s.replace(charToCount,'')
    
print (newS)
#w2 e1 a4 t3 c1 k1 d1 n1

#find the letter with highest char
#each one is a word. loop thru word.
loopS = newS
highLetter = ''
highCount = 0
index = 0
sortedS = ''
for j in range(countOfChars):
    highLetter = ''
    highCount = 0
    index = 0
    for i in range(countOfChars - j) :
        
        #the count can be one or more digits. So, find all the digits until space.
        #for now, just make it single digit
        count = int(loopS[index + 1])
        if(count > highCount):
            highCount = count
            highLetter = loopS[index]
        #go to the next word
        index += 3 #extra for space
    sortedS = sortedS + highLetter +  str(highCount ) + ' '
    print (sortedS)
    #remove highLetter from loopS
    loopS = loopS.replace(highLetter +  str(highCount ) + ' ','')
    print (loopS)
    print ('-----')
print (sortedS)



