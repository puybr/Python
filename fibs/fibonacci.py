def fibs(n):
    if n==0: return 0
    if n==1: return 1
    else: return fibs(n-1)+fibs(n-2)

def output(n):
    arr = []
    arr.append(fibs(n))
    while n > 0:
        n = n - 1
        arr.append(fibs(n))
    arr.reverse()
    return arr


print(output(12))