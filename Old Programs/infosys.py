"""inp=input("enter the string")
if(inp[-1]=='g' and len(inp)>=3):
    inp=inp+"ly"
    print(inp)
elif (len(inp)>3):
    inp=inp+"ing"
    print(inp)
else:
    print(inp)"""
#PF-Prac-1
#PF-Prac-1
def add_string(str1):
    if(str1[-1]=='g' and len(str1)>=3):
        str1=str1+"ly"
        return str1
    elif(len(str1)>3):
        str1=str1+"ing"
        return str1
    else:
        return str1
str1="end"
print(add_string(str1))