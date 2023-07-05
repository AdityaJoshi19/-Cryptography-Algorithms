#Aditya R Joshi | A207 | 70012000190 | BTech IT 3rd Year

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain_text,key):
    cipher_text = ""
    for i in plain_text:
        if i in alpha:
            idx = alpha.index(i)
            idx = (idx + key)%26
            cipher_text = cipher_text + alpha[idx]

        elif i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx + key)%26
            cipher_text = cipher_text + ALPHA[idx]

        else:
            cipher_text = cipher_text + i
    print("Text encrypted: "+cipher_text)
    
def decrypt(cipher_text,key):
    plain_text = ""
    for i in cipher_text:
        if i in alpha:
            idx = alpha.index(i)
            idx = (idx - key)%26
            plain_text = plain_text + alpha[idx]

        elif i in ALPHA:
            idx = ALPHA.index(i)
            idx = (idx - key)%26
            plain_text = plain_text + ALPHA[idx]

        else:
            plain_text = plain_text + i
    print("Text decrypted: "+plain_text)

choice = 3
while(choice != 0):
    choice = input("\n\nWhat operation you want to perform: \n For Encryption - Enter 1 \n For Decryption - Enter 2 \n For Exit - Enter 0 \n ")
    match choice:
        case "1":
            text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            key = int(key)
            encrypt(text,key)

        case "2":
            text = input("Enter the cipher text: ")
            key = input("Enter the key: ")
            key = int(key)
            decrypt(text,key)

        case "0":
            print("Thank you using the program")
            choice = 0