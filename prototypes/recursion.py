num = 1
fac = 5
"""
for i in range(factorial, 1, -1):
    num *= i
print(num)


def factorial(i, n):
    if i > 0:
        n *= i
        i -= 1
        return factorial(i, n)
    else:
        return n

print(factorial(5, 1))


def factorial2(i):
    # 1. stopping condition, you don't recrusive, otherwise you have an infinite
    # loop
    if i == 1:
        return 1
    # 2. resursive step, you call the same function with a simpler problem
    else:
        return factorial2(i - 1) * i

    
print(factorial2(5))


# ---------------------------------------
"""
def myindex(array, tofind, i=0):
    if i == len(array):
        return None
    else:
        if array[i] == tofind:
            return i
        else:
            return myindex(array, tofind, i + 1)
    
    
print(myindex([1, 2, 3, 4, 5, 6], 4))

def myindexloop(array, tofind):
    for i in range(len(array)):
        if array[i] == tofind:
            return i
print(myindexloop([1, 2, 3, 4, 5, 6], 4))


        