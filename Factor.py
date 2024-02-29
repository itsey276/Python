def Factor(n):
    def Factor_iter(i):
        if i * i > n:
            return n
        elif n % i == 0:
            print(i)
            return n / i
        else:
            i += 1
            return Factor_iter(i)
    result = Factor_iter(2)
    if result == n:
        print(int(result))
    else:
        Factor(result)

Factor(84)

    



