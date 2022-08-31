from ftplib import error_temp
from pickle import TRUE


s1 = input("Enter first string ")
s2 = input("Enter second string ")
errmsg = "No common chars"
#commonChars = ""
commonCharFound = False

for i in range(0, len(s1)):
    s1char = s1[i]
    for j in range(0, len(s2)):
        s2char = s2[j]
        if( s1char == s2char):
           print(s1char)
           commonCharFound = TRUE
           # commonChars+=s1char
        
#    
#print(commonChars) 
if(not (commonCharFound)):
    print(errmsg)