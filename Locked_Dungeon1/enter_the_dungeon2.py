#!/usr/bin/env python

import argparse
from hashlib import sha256
from Crypto.Cipher import AES
import os
import sys

def exploit(flag,flag_size):

    flag=flag
    flag_size=flag_size
    user_input=''
    bl_size=16
    ctext=aescipher.mod_encrypt(flag + user_input, flag_size)
    ctext_len=len(ctext)/2
    i=1   

    while(bl_size<ctext_len):

        user_input='a'*i
        ctext=aescipher.mod_encrypt(flag + user_input, flag_size)
        bl_size=len(ctext)/2
        i+=1

    flag_len=(bl_size)-(i+1)
    fixed_inp=(48-flag_len)*'a'
    pt='' 

    for j in range(flag_len-1,-1,-1):

        user_input='a'*j+fixed_inp
        check_block=aescipher.mod_encrypt(flag + user_input, flag_size)

        for char in range(256):

            user_input=pt+chr(char)+'a'*j+fixed_inp
            attack_block=aescipher.mod_encrypt(flag + user_input, flag_size)
            if attack_block==check_block:
                pt+=chr(char)
                break

    print(pt)


BLOCK_SIZE = 16
PAD_LIMIT = 48
KEY = os.urandom(16)

pad_len = lambda inp: (BLOCK_SIZE - len(inp) % BLOCK_SIZE)
pad = lambda inp: inp + chr(pad_len(inp))*pad_len(inp)


class AESCipher:
    def __init__(self, key):
        self.key = sha256(key).digest()

    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return "".join("{:02x}".format(ord(c)) for c in cipher.encrypt(raw))

    def mod_pad(self, inp, flag_size):
        input_len = len(inp)
        if input_len > PAD_LIMIT:
            excess_len = input_len - PAD_LIMIT
            if excess_len > flag_size:
                padded_inp = inp[flag_size:flag_size + PAD_LIMIT]
            else:
                padded_inp = inp[:flag_size - excess_len] + inp[flag_size:]
            return padded_inp
        else:
            padded_inp= pad(inp)
            return padded_inp

    def mod_encrypt(self, raw, flag_size):
        raw = self.mod_pad(raw, flag_size)
        encrypted_data = self.encrypt(raw)
        return encrypted_data

if __name__ == "__main__":
   
    with open("flag.txt") as fp:
        flag = fp.read()
    flag_size = len(flag)
    if flag_size > PAD_LIMIT:
        print("Flag is too big")
        exit(1)
    aescipher = AESCipher(key=KEY)
    exploit(flag,flag_size)
    
