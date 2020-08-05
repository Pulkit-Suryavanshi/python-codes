num=int(input("Enter the lengnth of the list"))
list1=[]
for x in range(num):
    list1.append(int(input()))
print(list1)
tr=0
y=0
for y in range(num):
    if(list1[y]==1):
        if(list1[y+1]==2):
            if(list1[y+2]==3):
                print("True")
                tr=tr+1
if (tr==0) :
    print("False")