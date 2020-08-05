def denom(arr):
    for i in arr:
        sum = 0
        count=0
        for j in range(1,i):
            sum=sum+j
            count+=1
            if(sum>=i):
                break
            else:
                continue
        print(count)

if __name__ == '__main__':
    arr=list()
    tc=int(input())
    for p in range(tc):
        arr.append(int(input()))
    denom(arr)