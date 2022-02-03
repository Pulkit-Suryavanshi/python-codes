def shellSort(a,n):
    g=n//2 #gap calculation
    while g>0:
        for x in range(g,n):
            y=a[x] # selecting the element at that gap
            z=x # storing the index of that gap element
            while z>=g and a[z-g]>y: # while the index is greater than gap and element(at z-g)>element at gap
                a[z]=a[z-g] #set that gap element as a[z-g]
                z-=g #decreasing index
            a[z]=y
        g//=2 # reducing the gap /2 /4 /8

a=[4,1,9,10,2]
shellSort(a,len(a))
print(a)
