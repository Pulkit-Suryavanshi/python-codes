inp=list(map(int,input().split()))
flag=0
for i in range(0,len(inp)-1):
    if(inp[i]==1):
        if(inp[i+1]==2):
            if(inp[i+2]==3):
                flag += 1
if (flag = 0):
    print(False)
else:
    print(True)