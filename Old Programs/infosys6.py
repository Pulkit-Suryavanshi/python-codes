inp = list(map(int,input().split()))
for i in range(len(inp)):
    if(inp[i]==1):
        if(inp[i+1]==2):
            if(inp[i+2]==3):
                print(True)
                break
            else:
                print(False)
                break
        else:
            print(False)
            break
    else:
        print(False)