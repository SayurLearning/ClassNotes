#10th student pass - mark above 35 in all subjects. We only have 2 subjects

#new condition - if above 95 in English or Tamil, its pass.

#new condition for FirstClass pass - 
# Tamil more than 85 and English more than 65
#Tamil more than 65 and English more than 85 

#newcondition - Tamil is between 70 to 90 and English between 50 to 70 , is first class.

tamilMark = int(input("Enter Tamil mark: "))
englishMark = int(input("Enter English mark: "))
totalMarks = tamilMark + englishMark
passmark = 35
#pass condition
#Condition - comparing two things

 tamilMark >= 70


if (( tamilMark >= 85 and englishMark >= 65 ) or (tamilMark >= 65 and englishMark >= 85 )):
    print("First class")

if ((  tamilMark >= 70 and tamilMark <= 90) and (englishMark >=50 and englishMark <=70)) :
    print ("First class")

if( ( (tamilMark >= 95) or (englishMark >= 95) ) or  

 ((tamilMark >= passmark ) and (englishMark >= passmark)) ):
    print ("pass")
else:
    print("fail")

'''
#writing code in many if statements. Nested if is can be done using And condition.
if(tamilMark >= passmark):
    #begin if Tamil mark is pass
    if(englishMark >= passmark):
        print("pass")
    else:
        print("failed in English")
    #end
else: #Tamil is less than passmark
    print (" Failed in Tamil")
'''
       
         
'''  

if(tamilMark >= passmark and englishMark >= passmark):
    #begin
    print("Pass")
    #end
elif ( totalMarks >= 90 and tamilMark >= 25 and englishMark >=25  ):
    #begin
    print("pass")
    #end
else:
    #begin
    print("Fail")
    #end
'''