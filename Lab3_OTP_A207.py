# Aditya R Joshi | A207 | 70012000190 | BTech IT 
import random
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plain_text):
    key = ""
    cipher_text = ""
    int_list = []
    key_list = []
    plain_text = plain_text.upper()
    for i in range(0, len(plain_text)):
        a = random.randint(0,25)
        int_list.append(a)

    for i in int_list:
        key = key + ALPHA[i]
        key_list.append(ALPHA[i])

    for i in range(0,len(plain_text)):
        idx = (ALPHA.index(plain_text[i])  +  ALPHA.index(key_list[i])) % 26
        cipher_text = cipher_text + ALPHA[idx]
    print("Key generated: ",key)
    print("Cipher text generated: ",cipher_text)

def decrypt(key, cipher_text):
    plain_text = ""
    key_list = []
    int_list = []
    for i in key:
        key_list.append(i)

    for i in range(0,len(cipher_text)):
        idx = (ALPHA.index(cipher_text[i])  -  ALPHA.index(key_list[i])) % 26
        plain_text = plain_text + ALPHA[idx]
    
    print("Plain text decrypted: ", plain_text)

print("----------ENCRYPTION----------")
plain_text = input("Enter the Plain Text: ")
encrypt(plain_text)
print("------------------------------")
print("------------------------------")
print("----------DECRYPTION----------")
key = input("Enter the key: ")
cipher_text = input("Enter the cipher text: ")
decrypt(key,cipher_text)