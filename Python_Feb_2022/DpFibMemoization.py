def fib(n, memoizationD):
    if n in memoizationD:
        return memoizationD[n]
    if n is 0 or n is 1:
        return 1
    else:
        memoizationD[n] = fib(n - 1, memoizationD) + fib(n - 2, memoizationD)
        return fib(n - 1, memoizationD) + fib(n - 2, memoizationD)


print("fib: 0,1,1,2,3,5,8,13,21,34,55,89,144...")
memo = {}  # declaring the memoization dictionary which will hold recursive values
num = int(input("Enter the fibonacci term you want after 0,1: "))
print(fib(num, memo))
# 34 takes time
