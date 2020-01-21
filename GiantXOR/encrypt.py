from os import urandom
import string

key = ""

def get_key(keylength):
    global key
    c = urandom(1)
    if len(key)!=keylength:
        if c not in string.ascii_lowercase and c not in string.ascii_uppercase:
            get_key(keylength)
        else:
            key += c
            get_key(keylength)

def multiplyKey(pt, k):
    while len(k) < len(pt):
        k += k
    k = k[:len(pt)]
    return k

def encrypt(plaintext, k):
    ciphertext = ""
    plaintext = plaintext.encode("base64")
    k = multiplyKey(plaintext, k)
    assert len(k) == len(plaintext)
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext) ^ ord(k))
    return ciphertext.encode("hex")

secret_flag = open("flag.txt",'r').read().strip()
keylength = int(open("keylength.txt",'r').read().strip())
get_key(keylength)
ciphertext = encrypt(secret_flag, key)

object1 = open("ciphertext.txt",'w').write(ciphertext)
