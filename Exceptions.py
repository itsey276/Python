a = 10
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("Divide by zero error")
except:
    print("Something else went wrong")
else: 
    print(c)
finally:
    print (a, "/", b)

    


