# Aditya Joshi 
alpha = "abcdefghijklmnopqrstuvwxyz"

def columnar(pt,key):
    pt = pt.lower()
    key = key.lower()
    ptsize = len(pt)
    keysize = len(key)
    dict = {}
    for i in key:
        dict[i] = ""

    if ptsize % keysize != 0:
        for i in range(0,(keysize - (ptsize%keysize))):
            pt = pt + "z"      #adding fillers
    
    rows = ptsize//keysize

    for i in range(0,keysize):
        temp = i
        while(temp == rows):
            dict[key[i]] = dict[key[i]] + pt[temp]
            temp += keysize
    print(dict)

pt = input("Enter the plain text: ")
key = input("Enter the key: ")
columnar(pt,key)