#Aditya R Joshi | A207 | 70012000190 | BTech IT 3rd Year

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
key_str = []

def evaluate_key(plain_text,key):
    x = 0
    key = key.upper()
    for i in range(0,len(plain_text)):
        key_str.append(key[x])
        x = (x+1) % len(key)

def encrypt(plain_text,key):
    plain_text = plain_text.upper()
    cipher_text = ""
    x = 0
    for i in plain_text:
        if i in alpha:
            idx = (alpha.index(i) + alpha.index(key_str[x])) % 26
            cipher_text = cipher_text + alpha[idx]
            x += 1

        elif i in ALPHA:
            idx = (ALPHA.index(i) + ALPHA.index(key_str[x])) % 26
            cipher_text = cipher_text + ALPHA[idx]
            x += 1
        
        else:
            cipher_text = cipher_text + i
            x += 1
    print("Encrypted text : "+cipher_text)

def decrypt(cipher_text,key):
    cipher_text = cipher_text.upper()
    plain_text = ""
    x = 0
    for i in cipher_text:
        if i in alpha:
            idx = (alpha.index(i) - alpha.index(key[x])) % 26
            plain_text = plain_text + alpha[idx]
            x += 1

        elif i in ALPHA:
            idx = (ALPHA.index(i) - ALPHA.index(key[x])) % 26
            plain_text = plain_text + ALPHA[idx]
            x += 1
        
        else:
            plain_text = plain_text + i
            x += 1
    print("Decrypted text : "+plain_text)
# evaluate_key("aditya joshi", "adi")
# encrypt("aditya joshi", "adi")

choice = 3
while(choice != 0):
    choice = input("What operation you want to perform: \n For Encryption - Enter 1 \n For Decryption - Enter 2 \n For Exit - Enter 0 \n ")
    match choice:
        case "1":
            text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            evaluate_key(text,key)
            encrypt(text,key_str)

        case "2":
            text = input("Enter the cipher text: ")
            key = input("Enter the key: ")
            evaluate_key(text,key)
            decrypt(text,key_str)

        case "0":
            print("Thank you using the program")
            choice = 0