def app_and_del(s, t, k):
    s_length = len(s)
    t_length = len(t)

    if s_length + t_length < k: return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l:
            same += 1
        else:
            break

    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2: return 'Yes'
    return 'No'


print(app_and_del(s, t, k))
'''i think it's easier to explain with an example. say you want to get'abcde' from
'abc'. the difference is 2, which is even (2%2==0). i can only have a k value
that is even to reach abcde, any odd number won't work.
 likewise if i wanted to reach abcd (1%2==1), only an odd k would work. hope this clears it up'''

'''numSameChars = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        numSameChars = i-1
        break

diff = len(s)-numSameChars + len(t)-numSameChars
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')'''