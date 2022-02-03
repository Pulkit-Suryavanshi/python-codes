# selection sort:
def selSort(a):
    for x in range(len(a)):
        minimum=x
        for y in range(x+1,len(a)):
            if a[y]<a[minimum]:
                minimum=y
        (a[x],a[minimum])=(a[minimum],a[x])
a=[2,8,1,6,10,0]
selSort(a)
print(a)