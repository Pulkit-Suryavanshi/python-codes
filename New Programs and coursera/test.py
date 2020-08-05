def isSubSequence(string1, string2, m, n):
    if m == 0: return True
    if n == 0: return False

    if string1[m - 1] == string2[n - 1]:
        return isSubSequence(string1, string2, m - 1, n - 1)
    return isSubSequence(string1, string2, m, n - 1)

if __name__=="__main__":
    d=list(map(str,input().split()))
    string2=input()
    maxlen=""
    for string1 in d:
        m = len(string1)
        n = len(string2)
        if isSubSequence(string1, string2, m, n):
            if (len(maxlen)<m):
                maxlen=string1
    print(maxlen)