# Locked Dungeons1
## Overview

On the first glance itself you briefly get an idea that encryption program is an implementatioin of a modified AES-ECB encryption oracle along with the standard PKCS#11 padding.

Declared inside the class AESCipher we can observe the two functions which are the core part of the challenge i.e the `mod_encrypt` and the `mod_pad` functions.
furthermore we observe that the user can input some values.

Also notice that after the flag file is read certain conditions are being checked:
- Flag size should be less than 48.
- user can input 6400 times.
- user input should not be greater than 100.

Further more we observe a sys call which writes the result of `mod_encrypt` function 
to stdout.

## The Approach

So now that we have an overall idea of the challenge lets dive into the solution:
First lets analyse the **enryption** function:
 
 The very first thing that catchtes the eye is what the functiosn returns-
 ```python
 "".join("{:02x}".format(ord(c)) for c in cipher.encrypt(raw))
 ```
 What this piece of code essentially does is takes each character in the ciphertext and encodes it into hex.
 So now we know the output will be the hex encoded ciphertext.
 
 So thats done. Now lets move on to the *real interesting part of the problem!!*
 THE `mod_pad` function!!
 ### Analysing mod_pad
 Lets analyse the code step by step:
 
```python
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
```

First the input length is being checked to determine if it is **greater than 48**.
If it is, then the excess length is calculated and then two further conditions are being checked out of this the former
one is not so important as such as we will see soon.(*as to get the answer we only need to satisfy the latter of the two conditions*)

**NOTE**: *plaintext = flag + user_input*.

What the else condition does is adds two modified parts of plaintext.
The first part `inp[:flag_size - excess_len]` creates a string in which the flag is present but depending on the excess length that many characters are replaced from the end (*i.e from right to left*) by the user input.
The second part `inp[flag_size:]` is just taking the user input present after the flag string and adding it to the first part.

so just think if the user input is such that the excess length is **flag_size-1** then the cipher text will start with the first character of flag follwed by 47 user input characters (lets take that to be *a*) so we get *ciphertext* = `first_chr_of_flag+'a'*47` .

Now if you have been following the writeup crystal clear you probably know whats the solution and assuming you have
then yup its nothing other than the famous ***ECB byte at a time attack!!!!*** a rather twisted version of it but the core logic is same.

Here we implement the attack from the first character of the ciphertext by setting the initial excess length to **flag_size-1** and then we iterate in a loop and on each iteration excess length is reduced by one therby exposing one extra character of the flag each time.

AND VOILLA YOU GET THE FLAG: `ctfFlag{Vishvesh_S_Rao}`

in this case it is my own flag that i had to set as i couldnt `nc` to get the actual flag file :)







