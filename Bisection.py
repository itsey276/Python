def y(x):
   return x*x - 2

epsilon = 0.0001
a = 0
b = 7
guess = 1
result = y(guess)

if y(a) * y(b) > 0:
    print("No root found!")
    exit(0)

while abs(result) > epsilon:
    if y(a) * result > 0: 
        a = guess
    else: 
        b = guess
    guess = (a + b) / 2
    result = y(guess)

print(b)







