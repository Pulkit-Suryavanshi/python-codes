if __name__ == '__main__':
    lb, ub, i, j, flag = 0, 0, 0, 0, 0
    arr = list(map(int, input().rstrip().split()))
    prime=list()
    nprime=list()
    new=0
    new1=0
    counting=0
    answer=list()
    prime2=list()
    for i in range(arr[0], arr[1] + 1):
        if (i == 1):
            continue
        flag = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break
        if (flag == 1):
            prime.append(i)
    print(prime)
    #prime=[2,3,5,7,11,13,17,19,23,29]
    #for making new combinations !
    for i in prime:
        for j in prime:
            if(i==j):
                continue
            new=str(i)+str(j)
            new1=int(new)
            if not new1 in nprime:
                nprime.append(new1)
    print(nprime)
    #finding prime in new combination list
    for i in nprime:
        flag = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break
        if (flag == 1):
            prime2.append(i)
    print(prime2)
    #following asked in question
    count=len(prime2)
    n1=min(prime2)
    n2=max(prime2)
    nth=0
    #finding fibonacci till count terms
    while counting < count:
        answer.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    largest=max(answer)
    print(largest)