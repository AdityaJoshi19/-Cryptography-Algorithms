# Aditya R Joshi | A207 | 70012000190 | BTech IT 

print("***NOTE*** \n1. 'p' and 'g' must be large prime numbers. \n2. 'p' and 'g' must not be equal. \n3. 'p' must be greater than 'g'\n")
p = int(input("Enter the value for 'p': "))
g = int(input("Enter the value for 'g': "))

a = int(input("Enter the value for 'a': "))
b = int(input("Enter the value for 'b': "))

A = (g**a)%p
B = (g**b)%p

k1 = (B**a)%p
k2 = (A**b)%p

if k1 == k2:
    print("Key Shared Successfully")
    print("Key is :",k1)
else:
    print("Key not found")