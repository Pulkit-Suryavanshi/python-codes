n=int(input())
a=[]
percent=0
dict={}
for i in range(n):
    a.append(input().split(" "))
for j in a:
    lol=float(j[1])+float(j[2])+float(j[3])
    lol2=(lol/300)
    percent=lol2*100
    rest=j[0]
    dict[j[0]] = ('%.2f'%percent)
    #dict.update({j[0]:percent})
ser=input()
print(dict[ser])