def bs(mylist):
    b=len(mylist)-1
    for x in range(b):
        for y in range(b-x):
            if(mylist[y]>mylist[y+1]):
                mylist[y],mylist[y+1]=mylist[y+1],mylist[y]
    return mylist
mylist=[5,1,2,7,9,3]
print(bs(mylist))