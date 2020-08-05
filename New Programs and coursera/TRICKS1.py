


'''
The zfill() method adds zeros (0) at the beginning
of the string, until it reaches the specified length.
If the value of the len parameter is less than
the length of the string, no filling is done.
'''

'''# function returning binary string
def Binary(n):
    s = bin(n)

    # removing "0b" prefix
    s1 = s[2:]
    return s1

    convert to binary'''

'''j = int(bin(i)[2:].replace('1','9'))
for converting 1 to infinite i from binary to multiple of n ranges 9and0 pattern
'''

'''for method in [str.isalnum, str.isalpha, str.isdigit, str.islower,
str.isupper]:
    print any(method(c) for c in s)
    for checking if string entered is'''

'''def count_substring(string, sub_string):
    match = re.findall('(?='+sub_string+')',string)
    return (len(match))
    matching substring'''

'''(?=...)
Matches if ... matches next, but doesn’t consume any of the string.
This is called a lookahead assertion. For example, Isaac (?=Asimov)
will match 'Isaac ' only if it’s followed by 'Asimov'
in findall'''
'''string=string[:position]+c+string[(position+1):]
to change a string on position with a character

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
also applicable'''
'''for i,j in zip(x,y):
this will iterate all characters in x and y'''
"""n = input()
ans = [0] * 100
for i in [int(n) for n in input().split()]:
    ans[i] += 1
print(*ans)
"""

# to produce combinations of all elements in list in lists!
"""
import itertools

stuff = [1, 2, 3]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        print(subset)
"""