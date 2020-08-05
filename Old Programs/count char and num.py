sen=input("Enter the sentence in alphabets and numerics")
l=len(sen)
cn=0
ca=0
for x in sen:
    if (x in ("1234567890")):
        cn+=1
    elif x!="" and x in ("abcdefghijklmnopqrstuvwxyz"):
        ca+=1
list1=[ca,cn]
print(list1)