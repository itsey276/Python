
def isSubset(a, b):
    found = False
    for element in a:
        for item in b:
            if element == item:
                found = True
        if found == False:
            return False
        found = False
    return True

def union(a, b):
    d = []
    for element in a:
        if not isSubset([element], b):
            d.append(element)
    return b + d

def intersection(a, b):
    d = []
    for element in a:
        if isSubset([element], b):
            d.append(element)
    return d

def complement(a, b):
    d = []
    for element in b:
        if not isSubset([element], a):
            d.append(element)
    return d

def isEqual(a, b):
    if isSubset(a, b) and complement(a, b) == []:
        return True
    else:
        return False
    
def unRepeat(a):
    b = []
    for element in a:
        if element not in b:
            b.append(element)
    return b



a = ['a', 'b']
b = ['a', 'b', 'f']
c = ['a', 'b', 'c', 'd', 'e']
g = ['a', 'b', 'f']
l = ['a', 'a', 'b', 'b', 'e']

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("g: ", g)
print("l: ", l)

d = union(b, c)
e = intersection(b, c)
f = complement(a, c)
h = isEqual(b, g)
m = unRepeat(l)


print("The union of b and c: ", d)
print("The intersection of b and c: ", e)
print("The complement of a and c: ", f)
print("Are b and g equal? ", h)
print("l without repeats: ", m)



















