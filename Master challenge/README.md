# Master Challenge
## Overview 
This was one of the most interesting RSA challenges that I have solve till date. There are numerous points about this challenge that it make it so intriguing and unusual one of them being the hint (I will come to that later :p)  
One thing you would have noticed is how it seems that most of variables which have been used in the challenge script are not even acessible to the solver.

You would also notice that there are multiple ciphertexts, modlus, public exponents declared (some which we dont even know the value of). 

Lets list them out in the order we'll be finding them in:
1. ```P```
1. Public exponenets ```e1``` and ```e2```
1. Prime factors of ***n***(*mentioned as **n12** in the data file*):
   1. ```q1p```
   1. ```q1q```

1. The ```hint``` 
1. The ```flag```

All these variables might make this challenge look pretty baffling on the first glance but the key is solving it step by step getting each of the variable one(or two) at a time.

So lets get those variables *one at a time.........*

## The Approach1. Item 1
### 1. Retrieving P
