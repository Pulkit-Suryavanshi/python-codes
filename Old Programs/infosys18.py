d={"Euro":0.01417,
"British Pound":0.0100,
"Australian Dollar":0.02027,
"Canadian Dollar":0.02027
}
inp1=input()
inp2=int(input())
for i in d:
    if(i==inp1):
        rupee=inp2/d[i]
print(rupee)