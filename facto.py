def modsum(a):
    mod = 10**9 + 7
    return (a%mod)

def fact(n,dict):
    sum=0
    if n in dict:
        return dict.get(n)

    if (n==0 ):
        dict[n] = 1
        return 1
    else:
        sum = n*fact(n-1,dict)
    dict[n] = modsum(sum)
    return sum

if  __name__ == "__main__":
    import sys
    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(1000000000)
    tests = int(input().strip())
    dict = {}
    for z in range(tests):
        p = int(input().strip())
        fac = fact(p,dict)
        print(fac)
