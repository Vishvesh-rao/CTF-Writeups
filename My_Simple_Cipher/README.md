# My Simple Cipher

## Overview of the challenge

The challenge involved an encryption program which performed the following encryption to genereate the cipher text:

```**for i in range(0, len(message)):
  encrypted += chr((ord(message[i]) ^ ord(key[i % len(key)]) ^ ord(encrypted[i]))%128)**
```

***encrypted*** is the ciphertext and a random ascii character was added to it before the encryption loop.

The goal was to find the flag from a message which consisted essentially three parts
- The **flag** 
- A predefined character > **'|'**
- And a **key**
ctfFlag{Vishvesh_S_Rao}
An output of the encryption program was given which when hex decoded gave a ciphertext of length 36.
Consequently I found out the Length of the flag part by subtracting ciphertext length from key lentgth plus 2 (taking into account the predefined chracter 
**'|'**.
and the randomly generated ascii character) 

## The Approach

Since in the encryption equation there are two unknowns it seems impossible to find the key and hence the flag.
The idea here is that the program already gives us a character in the message namel the predefined character 
 **'|'**
whose position we know.
taking the position of that character as **'i'** value we can get the correspnding value of the character at index ***i%13*** in **key**. 
On the index counter of the list ***message*** the corresponding vlaue of **key[i%13]** will be at the position **message[22+i%13]** (*as **Key** comes after **flag** text and the predefined character*)

Now I have got **message[22+i%13]**.Now i can assign i to **i=22+i%13**. 
If I put these three instructions:
1. Finding value of **key[i%13]**
2. Assigning that value to **message[22+i%13]**
3. Changing value of **i** to **22+i%13**

In a loop that repets 12 times what we surprisingly get is nothing other than value of ***key*** in all its thirteen characters!!!

The core logic behind this piece of code is pretty easy **eliminate one unkown out of the two** which essentially solves the challenge to a *very large extent* .
Here the variable being elimnated is **messge[i]**.
We do this by assignig **message[index]** the value of the ***key*** which we find in the first loop instruction and consequently assigning that 
**i**
with value 
**index**
in the third loop instruction so that when the loop iterates the next time the value for **message[i]** is no longer an unknown thus we find out the entire key (***but not the full message***).

Now with only one unknown finding the complete ***message*** is childs play (just solve the encryption equation with **message[i]** as the unknown)

In the end we get the key as: ***ENJ0YHOLIDAY!***

Flag as: **TWCTF{Crypto-is-fun!}**

