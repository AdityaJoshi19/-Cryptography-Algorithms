#Aditya R Joshi | A207 | 70012000190 | BTech IT
# Product Cipher
# (RAILFENCE + CAESAR) Cipher

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
def f3_encrypt(pt):
    final_ct = ""
    pt = pt.upper()
    s1,s2,s3 = "","",""
    for i in range(0,len(pt)):
        if i%4 == 0:
            s1 = s1 + pt[i]
        elif i%2 == 1:
            s2 = s2 + pt[i]
        elif i%2 == 0 and i%4 != 0:
            s3 = s3 + pt[i]
    ct = s1+s2+s3
    print("Intermediate Cipher Text: "+ct)
    key = int(input("Enter the key: "))
    for i in ct:
        if i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx + key)%26
            final_ct = final_ct + ALPHA[idx]

        else:
            final_ct = final_ct + i
    print("Text encrypted with Product Cipher(Rail-fence + Caesar): "+final_ct)

def f4_encrypt(pt):
    final_ct = ""
    pt = pt.upper()
    s1,s2,s3,s4 = "","","",""
    for i in range(0,len(pt)):
        if i%2 == 0 and i%3 == 0:
            s1 = s1 + pt[i]
        elif i%2 != 0 and i%3 != 0:
            s2 = s2 + pt[i]
        elif i%2 == 0 and i%3 != 0:
            s3 = s3 + pt[i]
        elif i%2 != 0 and i%3 == 0:
            s4 = s4 + pt[i]
    ct = s1+s2+s3+s4
    print("Intermediate Cipher Text: "+ct)
    key = int(input("Enter the key: "))
    for i in ct:
        if i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx + key)%26
            final_ct = final_ct + ALPHA[idx]

        else:
            final_ct = final_ct + i
    print("Text encrypted with Product Cipher(Rail-fence + Caesar): "+final_ct)

def f5_encrypt(pt):
    final_ct = ""
    pt = pt.upper()
    s1,s2,s3,s4,s5 = "","","","",""
    for i in range(0,len(pt)):
        if i%8 == 0:
            s1 = s1 + pt[i]
        elif i%8 == 1 or i%8 == 7:
            s2 = s2 + pt[i]
        elif i%8 == 2 or i%8 == 6:
            s3 = s3 + pt[i]
        elif i%8 == 3 or i%8 == 5:
            s4 = s4 + pt[i]
        elif i%8 == 4:
            s5 = s5 + pt[i]
    ct = s1+s2+s3+s4+s5
    print("Intermediate Cipher Text: "+ct)
    key = int(input("Enter the key: "))
    for i in ct:
        if i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx + key)%26
            final_ct = final_ct + ALPHA[idx]

        else:
            final_ct = final_ct + i
    print("Text encrypted with Product Cipher(Rail-fence + Caesar): "+final_ct)


def f6_encrypt(pt):
    final_ct = ""
    pt = pt.upper()
    s1,s2,s3,s4,s5,s6 = "","","","","",""
    for i in range(0,len(pt)):
        if i%10 == 0:
            s1 = s1 + pt[i]
        elif i%10 == 1 or i%10 == 9:
            s2 = s2 + pt[i]
        elif i%10 == 2 or i%10 == 8:
            s3 = s3 + pt[i]
        elif i%10 == 3 or i%8 == 7:
            s4 = s4 + pt[i]
        elif i%10 == 4 or i%10 == 6:
            s5 = s5 + pt[i]
        elif i%10 == 5:
            s6 = s6 + pt[i]
    ct = s1+s2+s3+s4+s5+s6
    print("Intermediate Cipher Text: "+ct)
    key = int(input("Enter the key: "))
    for i in ct:
        if i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx + key)%26
            final_ct = final_ct + ALPHA[idx]

        else:
            final_ct = final_ct + i
    print("Text encrypted with Product Cipher(Rail-fence + Caesar): "+final_ct)

    
choice = 1
while(choice != 0):
    pt = input("Enter the plain text: ")
    choice = int(input("\nFrom which fence you want to encrypt (3 to 6) : "))
    match choice:
        case 3: 
            f3_encrypt(pt)
        
        case 4: 
            f4_encrypt(pt)

        case 5:
            f5_encrypt(pt)

        case 6:
            f6_encrypt(pt)

        case 0:
            print("Thank you for using our program.")