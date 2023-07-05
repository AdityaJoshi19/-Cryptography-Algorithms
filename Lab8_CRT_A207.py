print("***NOTE***")
print("Value of: \n a1 < m1 \n a2 < m2 \n a3 < m3 \n")
flag1 = 0
flag2 = 0
flag3 = 0

a1 = int(input("Enter the value of a1 : "))
m1 = int(input("Enter the value of m1 : "))

a2 = int(input("Enter the value of a2 : "))
m2 = int(input("Enter the value of m2 : "))

a3 = int(input("Enter the value of a3 : "))
m3 = int(input("Enter the value of m3 : "))

M = m1*m2*m3
print("\nValue of: \nM =",M)
M1 = M/m1
M2 = M/m2
M3 = M/m3

print("\nValue of:\nM1 =",M1,"\nM2 =",M2,"\nM3 =",M3)

MI1 = 0
MI2 = 0
MI3 = 0
for i in range(1,20):
    if (M1*i) % m1 == 1 and flag1 == 0:
        MI1 = i
        flag1 = 1

    if (M2*i) % m2 == 1 and flag2 == 0:
        MI2 = i
        flag2 = 1

    if (M3*i) % m3 == 1 and flag3 == 0:
        MI3 = i
        flag3 = 1
    
    if flag1 == 1 and flag2 == 1 and flag3 == 1:
        break

print("\nValue of:\nM(inverse)1 =",MI1,"\nM(inverse)2 =",MI2,"\nM(inverse)3 =",MI3)

X = ((a1*M1*MI1) + (a2*M2*MI2) + (a3*M3*MI3)) % M

    
print("\nThe value of X is: ",X)