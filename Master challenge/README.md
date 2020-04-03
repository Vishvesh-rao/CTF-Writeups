# Master Challenge
## Overview 
This was one of the most interesting RSA challenges that I have solve till date. There are numerous points about this challenge that it make it so intriguing and unusual one of them being the hint (I will come to that later :p)  
One thing you would have noticed is how it seems that most of variables which have been used in the challenge script are not even acessible to the solver.

You would also notice that there are multiple ciphertexts, modlus, public exponents declared (some which we dont even know the value of). 

Lets list them out in the order we'll be finding them in:
1. ```P```
1. Public exponenets ```e1``` and ```e2```
1. Prime factors of ***n*** (*mentioned as **n12** in the [data file](https://github.com/Vishvesh-rao/CTF-Writeups/blob/master/Master%20challenge/data.py)*):
   1. ```q1p```
   1. ```q1q```
1. The ```hint``` 
1. The ```flag```

All these variables might make this challenge look pretty baffling on the first glance but the key is solving it step by step getting each of the variable one(or two) at a time.

So lets get those variables *one at a time.........*

## The Approach
###  #1. Retrieving **```p```**

This one was quite intuitive especially since the ciphertexts and modulus have been give in lists the lengths
of which corresponds to 4.
This is just a direct implementation of [Hastards broadcast attack](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/)

```python
  f=lambda m,e,n,c:pow(m,e,n)==c
  assert(sum(map(f,[p]*4,[4]*4,n,c))==4)
```
The above code basically checks if `p`<sup>4</sup> `modn` == ```c``` for all 4 values of ```n``` and ```c```(taken from the lists) 

Moving on to the next unknwon.........

### #2. Retrieving **```e1```** and **```e2```**
Here is the part where we maybe slightly misled by the following lines of code:
```python
ee1 = 42
ee2 = 3
assert(pow(e1,ee1,n)==ce1)
assert(pow(e2+tmp,ee2,n)==ce2)
```
At first glance it looks like we can retrive ```e2+tmp``` easily since the exponent ```ee2```=3 but after implementation we see that ```e2+tmp``` is pretty big and is not susceptible to small exponent attack.
By thinking of small exponent attack we are on the right idea but the wrong path since this attack which is not working for ```ee2``` actually works for ```ee1```=42. A direct implementation gets us the value of ```e1```.
 
Going back to ```e2```, since ```e2+tmp``` is really big there is no way we can directly bruteforce tha value of ```e2``` but
but again we are on the right idea but wrong way of implementation as in, instead of bruteforcing for the value directly we   bruteforce to find the actul value of the ciphertext i.e the unmoded value which would be this ```ce2+k*n11``` by iterting for different values of **```k```** and matching this with ```(e2+tmp)```<sup>3</sup> we canget ```e2```. Following is the implementation of the idea: 
 ```python
 for k in range(100000):
	val = root(ce2+k*n11,3)
	if(val[1]):
		e2 = val[0] - tmp
```
Moving on to stage 3............

### #3 Retrieving **```q1p```** and **```q1q```**

For this there doesn't seem to be any way in which we can exploit the implementation to obtain the cipher text with out
```q1p``` and ```q1q``` and they are the prime factors of the modulus and to obtain them the on;y way is factorization
Since **n** is too long for normal factorization we use [fermats method](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/) and we immediately get both the factors.

Thereafter finding hint is just elementry RSA operation.
The hint as it turns out to be: 
**```orz...you.found.me.but.sorry.no.hint...keep.on.and.enjoy.it!```**
is pretty useless :), still we got the factors with which we proceed to the last and final stage............

### #4 Retrieving the **```flag```**
This is arguably the most difficult value to retrieve amongst all and with good reason.
All though it might look like its childs play to obin the flag as we know both the fctors of the modulus **```p```** and **```q1```** when we try decrypting we realize the flaw that is **`GCD(e1,(p-1)*(q1-1))`** turns out to be 14 if we try with e2 we
get the same result.

Moment I saw this my first reaction was _dividing_ `e2` ( or `e1`) by 14, this gives us a GCD of 1. good! 
Now we find the private exponent d. 
 NOTE:**we are finding this for e/14**
now decrypting with this d what we get is `flag`<sup>e2*d</sup>`mod p*q2`

But since this d was the modular inverse of (e2/14) and not e2 what we are left with is
-> `flag`<sup>14*(e2/14)*d</sup>`mod p*q2`
-> `flag`<sup>14</sup>`mod p*q2` as `(e2/14)*d`==1
Now if take the 14th root of flag we should end up with the pliantext
Doing that we get flag and then we convert it to bytes and what we get is.... well its gibberish!! Meaning flag<sup>14</sup>
is bigger than `p*q2`

That means thats not the right way of doing ( again we are on the right idea but wrong track :D )
so if flag power 14 is too big how about reducing the power............

Now lets take only q2 as the modulus. The idea here is that if q2 is less than `p*q2` we may be able to retrieve the flag
so here's what we do:
-> c_modq = c_flag mod q2  (c_flag referenced as c1 in challenge script)
this makes some changes which we will see
-> c_flag = `flag`<sup>e2</sup>`mod p*q2`
-> c_modq = (`flag`<sup>e2</sup>`mod p*q2`)`mod q2`
-> c_modq = (`flag`<sup>e2</sup>`mod q2`)`mod p*q2`
Now `gcd(e2,(q2-1))`=2
so again we divide e2/2 and find `inverse(e2/2,(q2-1))` and we get d ( for e2/2 )
-> `c_modq`<sup>d</sup> = (`flag`<sup>2*(e2/2)*d</sup>`mod q2`)`mod p*q2`
Hence we get (`flag`<sup>2</sup>`mod q2`)`mod p*q2`
since `q2<p*q2` we can ommit `mod p*q2`
-> `c_modq`<sup>d</sup> = `flag`<sup>2*(e2/2)*d</sup>`mod q2`
now assuming flag<sup>2</sup><q2 we can get `flag` by taking root

this is the exploit for the idea:
```python
q1 = q1p
c1_modq = c_flag % q1
GCD1 = gcd(e1,q1-1)
d1 = invert(e1/GCD1,q1-1)
c1_modq = pow(c1_modq,d1,q1)
flag = root(c1_modq,2)[0]
```
In the we get decrypted flag as: **`de1ctf{9b10a98b-71bb-4bdf-a6ff-f319943de21f}`**

Here is the complete [exploit](https://github.com/Vishvesh-rao/CTF-Writeups/blob/master/Master%20challenge/exploit.py)

