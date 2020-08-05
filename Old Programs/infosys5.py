inp=input()
a=0
n=0
ans=[]
for i in inp:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        a+=1
    if((ord(i)>=48 and ord(i)<=57)):
        n+=1
ans.append(a)
ans.append(n)
print(ans)