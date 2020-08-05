next=1
prev=0
sum=0
for i in range (0,5):
    for j in range (0,i+1):
        sum = prev + next
        prev = next
        next = sum
        print(sum,"", end="")
    print("\r")#starting of line
