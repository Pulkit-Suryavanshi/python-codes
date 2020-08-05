def jumpingOnClouds(c):
    count = -1
    i = 0
    while i < len(c):
        count += 1
        #done to increase path by two if 0 i+2
        if i < len(c) - 2 and c[i + 2] == 0:
            i += 1
        i += 1
        return count
    '''revisit jump dist=k and -2-1 if thunder(1) and -1 if normal(0)
    def jumpingOnClouds(c, k):
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy'''
if __name__=='__main__':
    #c=map(int(input.split()))
    c = list(map(int, input().rstrip().split()))
    ans=jumpingOnClouds(c)