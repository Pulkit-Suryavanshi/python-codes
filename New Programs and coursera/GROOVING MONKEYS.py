def GROOVINGMONKEY(arr):
    x=0
    y=arr #containing replaced value
    count = 0
    x=[0]*len(arr) #used as a buffer
    while(x!=arr):
        count+=1
        x=[0]*len(arr) # refresh the x
        for i in range(len(arr)):
            x[arr[i]-1]=y[i]
        y=x
    return count

if __name__=="__main__":
    t=int(input()) # no of test cases
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        result=GROOVINGMONKEY(arr)
        print(result)