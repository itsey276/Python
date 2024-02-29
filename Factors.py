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

print(phi(15))

