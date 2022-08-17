#!/usr/bin/env python
# coding: utf-8

# # Prime numbers
# 
# 
# The goal of this section is to expose the reader to two different solutions to one given computational problem. We will show two different algorithms that solve the same problem. 
#  
# We hope to illustrate that the question *Can we do better?* is important and has consequences for the programs we write. Also, we want to convey that programming is not just about knowing how to use the constructs of a given programming language, but that it is important to learn about well known methods to come up with better programs (one of the purposes of the course).
# 
# We will also write programs in Python for the two algorithms. For doing so we will need to define functions, to use integers and lists, and to use ```for``` loops and ```if``` statements. If you need to refresh how to use all of these we refer you to 
# the corresponding sections of [A Concise Presentation of Python](https://veronica-gaspes.github.io/Concise-Python/intro.html).
# 
# ## A definition
# 
# Prime numbers are natural numbers bigger than 1 that have only two factors: 1 and themselves. 
# 
# For example: 2, 3, 5, 7, 11, 17, 19 are all prime numbers. On the other hand, 9 is not: it has 3 as a factor (you can find this expressed in different ways: 9 is divisible by 3 or 3 is a divisor of 9 or 9 is a multiple of 3).
# 
# There is no closed expression to calculate prime numbers. But there are many computational problems that use prime numbers, so we need to be able to recognize prime numbers (decide whether a number is prime or not) and to generate prime numbers. 
# 
# ## A problem
# 
# We are interested in the problem of calculating all prime numbers smaller than or equal to a given bound. 
# 
# For example, given the bound 50 we want to calculate all prime numbers smaller than or equal to 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43 and 47.
# 
# ## A first solution
# 
# If we can test whether a number is prime or not then we can solve this problem by applying this test to all numbers smaller or equal to the bound and keeping all numbers that pass the test.
# 
# Given the definition of prime number, we can test whether a number $n$ is prime by looking at all numbers between $2$ and $n - 1$ and checking divisibility.
# 
# This rather vague description is an algorithm: it solves a problem by describing how to proceed in a way that takes only a finite number of well known operations.
# 
# ## A first program for the first solution
# 
# To be able to program this algorithm we need first to be able to test whether a number is prime or not. We will do this by defining a function that takes a number as argument and returns a boolean as result. The result is ```True``` exactly when the number is prime and ```False``` for all other numbers. 
# 
# 
# The function ```is_prime``` in the next cell does exactly that following the algorithm we discussed above:
# 
# > To decide whether a number is prime try to detect a factor that is not 1 or the number itself. The method for finding a factor tests all numbers between 2 and the number. The search for a factor is put to an end if a factor is found.
# 
# For positive numbers ```n``` and ```i```  the expression ```n % i == 0``` has value ```True``` exactly when  ```i```is a factor of ```n``` (```n``` is divisible by ```i``` or ```i``` is a divisor of ```n```.) 

# In[1]:


def is_prime(n):
    for i in range(2,n):
        if n % i == 0: return False
    return True


# In[2]:


print(is_prime(10))
print(is_prime(11))
print(is_prime(12))


# Given that prime numbers are integer numbers larger than 1, we do not expect to test other numbers. In other words, when we use this function in our programs we will never use it with non-integer numbers or with numbers smaller than 1.
# 
# ## A second program for the first solution
# 
# *Can we do better?*
# 
# Well yes!
# 
# A factor of $n$ cannot be larger than $\lfloor \sqrt{n} \rfloor$! So the loop does not need to explore numbers larger than 
# $\lfloor \sqrt{n} \rfloor$:

# In[3]:


import math


# In[4]:


def is_prime_better(n): 
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True


# In[5]:


print(is_prime_better(4))
print(is_prime_better(11))
print(is_prime_better(12))


# Does this have consequences? 
# 
# Try the following cell for different values of ```n``` and see whether you experience any difference between the time it takes to print the first value and the time it takes to print the second value. For numbers that have small factors both functions terminate early in both cases. For example, even numbers, no matter how large, have 2 as a factor so the ```for``` loop terminates during the first iteration (in both functions!).
# 
# You can try with values 97, 7919, 199933, 999331, 27644437, 479001599, 87178291199. All these examples are prime numbers so the for loop goes through all numbers in the range. This is called the *worst case* for an algorithm. 

# In[6]:


n =  10000000
print(is_prime_better(n))
print(is_prime(n))


# Most likely there was not much difference for the first ones: both ```True``` values come out immediatelly. But for the last two or three ones, the first ```True``` comes out more or less immediatelly while the second ```True```  takes more and more time.
# 
# This will become evident later on when we use this function to, for example, calculate the prime numbers below 1000000.
# 
# Now that we have this test for primality, we can implement the rest of the algorithm: to calculate all prime numbers smaller or equal than a given bound, test all numbers smaller or equal to the bound and keep the ones that are prime.
# 
# Our implementation is in the form of a function that takes the bound as an argument and returns a list with all prime numbers smaller or equal than the bound.
# 
# The function uses a loop to go through all numbers between 2 and the bound. 
# 
# The two definitions, one using ```is_prime``` and one using ```is_prime_better``` are in the same cell:

# In[7]:


def primes_under(n):
    res = []
    for i in range(2, n):
        if is_prime(i): res = res + [i]
    return res

def primes_under_better(n):
    res = []
    for i in range(2, n):
        if is_prime_better(i): res = res + [i]
    return res


# Observe that both definitions have nested loops: the function for testing whether a number is prime or not is itself a for loop and we use it on every turn of the loop.

# In[8]:


bound = 1000
print(primes_under_better(bound))
print(primes_under(bound))


# To avoid printing all the values when testing bigger bounds, we print only the last element in the list. Again, you should try the next cell for larger and larger bounds. You can start with 10000 and  double until the second line takes too much time. Try 10000, 20000, 40000, 80000, 160000. 

# In[9]:


bound = 100
print(primes_under_better(bound)[-1])
print(primes_under(bound)[-1])


# Use the next cell to run only the better one and see how long you can go increasing the bound! 
# 
# What is the largest prime number under 1000000?

# In[10]:


bound = 100000
# print(primes_under_better(bound)[-1])


# ## Another solution
# 
# There is a very old method for listing the prime numbers under a given bound. It is called [Erathostenes sieve](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). 
# 
# Given a list with all numbers it removes the ones that are multiples of some number. It does this in order, first removing the multiples of 2, then the multiples of 3, (4 has already been removed!), then the multiples of 5, (6 has already been removed), etc. As you can see, only the prime numbers remain!
# 
# Here you can see the successive lists the sieve builds for numbers smaller than 100:

# In[11]:


sieve0 = list(range(2,100)) 

# keep 2 and remove multiples of 2
sieve1 = sieve0[0:1] + [x for x in sieve0 if x % sieve0[0] != 0]

# keep 2 and 3 and remove multiples of 3
sieve2 = sieve1[0:2] + [x for x in sieve1[1:] if x % sieve1[1] != 0]

# keep 2, 3 and 5 and remove multiples of 5 
sieve3 = sieve2[0:3] + [x for x in sieve2[2:] if x % sieve2[2] != 0]

# keep 2,3,5,7 and remove multiples of 7
sieve4 = sieve3[0:4] + [x for x in sieve3[3:] if x % sieve3[3] != 0]

# kepp 2,3,5,7,11 and remove multiples of 11 (they were already removed: 99 mul 3, 88 mul 2 and 77 mul 7!)
sieve5 = sieve4[0:5] + [x for x in sieve4[4:] if x % sieve4[4] != 0]

print(sieve0)
print()
print(sieve1)
print()
print(sieve2)
print()
print(sieve3)
print()
print(sieve4)
print()
print(sieve5)


# ## A first program for the second solution
# 
# Of course we could implement this idea of building new lists until there are no more things to remove. But this algorithm is usually implemented by having one list: a list of booleans that indicate whether the index (position) is prime (True) or not (False).
# 
# To start with, everything from 2 on is set to true. Then, in each iteration multiples of the position of the next True value are set to False.
# 
# We can use this list to produce the list of primes below a bound. 

# In[12]:


def erathostenes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False,False] 
    for i in range(2, n):
        if sieve[i]:
            for j in range(2*i,n + 1,i):
                sieve[j] = False
    return sieve

def erathostenes_primes_under(n):
    primes = erathostenes(n)
    res = []
    for i in range(2,n+1):
        if primes[i]: res = res + [i]
    return res


# In[13]:


erathostenes_primes_under(10)[-1]


# ## A second program for the second solution
# 
# *Can we do better?* 
# 
# Well yes!
# 
# Again: we do not need to remove multiples of numbers over $\sqrt{n}$!

# In[14]:


def erathostenes_better(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False,False] 
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(2*i,n + 1,i):
                sieve[j] = False
    return sieve

def erathostenes_primes_under_better(n):
    primes = erathostenes_better(n)
    res = []
    for i in range(2,n+1):
        if primes[i]: res = res + [i]
    return res
            
        


# In[15]:


erathostenes_primes_under_better(100000)[-1]


# ## A third program for the second solution
# 
# *Can we do better?*
# 
# Well yes!
# 
# We do not need to start removing the *low* multiples of a given value! When removing the multiples of 11, say, we have already removed 11 * 2, 11 * 3, 11 * 5 and 11 * 7! We can start with 11 * 11!
# 

# In[16]:


def erathostenes_better_2(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False,False] 
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve

def erathostenes_primes_under_better_2(n):
    primes = erathostenes_better_2(n)
    res = []
    for i in range(2, n+1):
        if primes[i]: res = res + [i]
    return res


# In[17]:


erathostenes_primes_under_better_2(10000)[-1]


# But here is one more advantage with the sieve approach:
# 
# the list of boolean values is actually an implementation of the function that tests whether a number is prime or not. Once we calculate this list it is very easy to test whether a number is prime or not with just one operation.
# 
# 

# In[18]:


bound = 100000
isPrime = erathostenes_better_2(bound)


# In[19]:


print(isPrime[2])
print(isPrime[3])
print(isPrime[4])
print(isPrime[97])


# ## Summary
# 
# You have seen 2 different algorithms to solve the same problem and you have seen that for a given algorithm there are details that can make it better!
