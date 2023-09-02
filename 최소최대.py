import math ## 꼭 외우기!! 

a, b = map(int, input().split())

def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            return i
            break

def lcm(a,b):
    return a*b//gcd(a, b)

print(gcd(a,b))
print(lcm(a,b))