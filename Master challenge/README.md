# Master Challenge
## Overview 
This was one of the most interesting RSA challenges that I have solve till date. There are numerous points about this challenge that it make it so intriguing and unusual one of them being the hint (I will come to that later :p)  
One thing you would have noticed is how it seems that most of variables which have been used in the challenge script are not even acessible to the solver.

You would also notice that there are multiple ciphertexts, modlus, public exponents declared (some which we dont even know the value of). 

Lets list them out in the order we'll be finding them in:
1. ```P```
1. Public exponenets ```e1``` and ```e2```
1. Prime factors of ***n*** (*mentioned as **n12** in the data file*):
   1. ```q1p```
   1. ```q1q```
1. The ```hint``` 
1. The ```flag```

All these variables might make this challenge look pretty baffling on the first glance but the key is solving it step by step getting each of the variable one(or two) at a time.

So lets get those variables *one at a time.........*

## The Approach
###  #1. Retrieving P

This one was quite intuitive especially since the ciphertexts and modulus have been give in lists the lengths
of which corresponds to 4.
This is just a direct implementation of [Hastards broadcast attack] https://github.com/Vishvesh-rao/Crypto-Exploits-Attacks/blob/master/Hastards.py

```python
  f=lambda m,e,n,c:pow(m,e,n)==c
  assert(sum(map(f,[p]*4,[4]*4,n,c))==4)
```
The above code basically checks if ```p<sup>4</sup>modn``` == ```c``` for all 4 values of ```n``` and ```c```(taken from the lists) 

Moving on to the next unknwon.........

### #2. Retrieving e1 and e2
Here is the part where we maybe slightly misled by the following lines of code:
```python
ee1 = 42
ee2 = 3
assert(pow(e1,ee1,n)==ce1)
assert(pow(e2+tmp,ee2,n)==ce2)
```
At first glance it looks like we can retrive ```e2+tmp``` easily since the exponent ```ee2```=3 but after implementation we see that ```e2+tmp``` is pretty big and is not susceptible to small exponent attack.
 By thinking of small exponent attack we are on the right idea but the wrong path since this attack which is not working for ```ee2``` actually works for ```ee1```=42. A direct implementation gets us the value of ```e1```.
 
 Going back to ```e2``` since ```e2+tmp``` is really big there is no way we can directly bruteforce tha value of ```e2``` but
 but again we are on the right idea but wrong way of implementation as in, instead of bruteforcing for the value directly we   bruteforce to find the actul value of the ciphertext i.e the unmoded value which would be this ```ce2+k*n11``` by iterting for different values of **```k```** and matching this with ```(e2+tmp)<sup>3</sup>``` we canget ```e2```. Following is the implementation of the idea: 
 ```python
 for k in range(100000):
	val = root(ce2+k*n11,3)
	if(val[1]):
		e2 = val[0] - tmp
```
