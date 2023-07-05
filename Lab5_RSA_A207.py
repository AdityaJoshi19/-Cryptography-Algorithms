# Aditya R Joshi | A207 | 70012000190 | BTech IT 

alpha = "abcdefghijklmnopqrstuvwxyz"
e_selection = []

def calculation(p,q):
    n = p*q
    phi_n = (p-1)*(q-1)
    for i in range(2,phi_n):
        if phi_n % i != 0:
            e_selection.append(i)
    select_e(phi_n,n)

def select_e(phi_n,n):
    n = n
    phi_n = phi_n
    print(e_selection)
    e = int(input("Select the value of 'e' from the above list: "))
    if e in e_selection:
        calculate_d(e,phi_n,n)
    else:
        print("-----  Selection error! Select value for 'e' from the given list!  -----")
        select_e(phi_n)

def calculate_d(e,phi_n,n):
    n,e = n,e
    phi_n = phi_n
    m = phi_n
    c,flag = 1,1
    while(flag):
        if (m+1)%e == 0:
            d = int((m+1)/e)
            flag = 0
        else:
            c = m+c
    choice = 3
    while(choice != 0):
        choice = input("\n\nWhat operation you want to perform: \n For Encryption - Enter 1 \n For Decryption - Enter 2 \n For Exit - Enter 0 \n ")
        match choice:
            case "1":
                encryption(e,d,n)

            case "2":
                decryption(e,d,n)

            case "0":
                print("Thank you using the program")
                choice = 0

def encryption(e,d,n):
    e,d,n = e,d,n
    pt = input("Enter the Plain Text: ")
    for i in alpha:
        if i == pt:
            pti = alpha.index(i)
            break
    cti = (pti**e)%n
    for i in range(len(alpha)):
        if i == cti:
            ct = alpha[cti]
            print("Cipher Text:",ct)

def decryption(e,d,n):
    ct = input("Enter the Plain Text: ")
    for i in alpha:
        if i == ct:
            cti = alpha.index(i)
            break
    pti = (cti**d)%n
    for i in range(len(alpha)):
        if i == pti:
            pt = alpha[pti]
            print("Plain Text:",pt)

p = int(input("Enter the value of P: "))
q = int(input("Enter the value of Q: "))
calculation(p,q)