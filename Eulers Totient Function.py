from math import floor

def factors(num):

    factorslist = []

    def prime(n):
        def prime_iter(i):
            if n % i == 0:
                return i
            elif i*i > n:
                return True
            else: 
                return prime_iter(i + 1)
        return prime_iter(2)
    
    def factors_iter(remainder):
        p = prime(remainder)
        if p == True:
            if remainder in factorslist:
                return factorslist
            else:
                factorslist.append(int(remainder))
                return factorslist
        else:
            factorslist.append(p)
            return factors_iter(remainder / p)
        
    return factors_iter(num)

def phi(n):
    phi_buffer = n
    factorslist = factors(n)
    for factor in factorslist:
        phi_buffer *= 1 - 1/factor
    return floor(phi_buffer)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

def Euler(a, n):
    assert gcd(a, n) == 1
    print("a =", a, ";", "n =", n)
    p = phi(n)
    print("Phi(" + str(n) + ") = ", p)
    left = a ** p % n
    print(a, "^", p, "mod", n , "=", left)
    right = 1 % n
    print("1 mod ", n, "=", right)

Euler(4, 9)
print("============")
Euler(3, 8)
print("============")
Euler(5, 9)
print("============")
Euler(3, 9)




