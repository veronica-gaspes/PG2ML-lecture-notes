#!/usr/bin/env python
# coding: utf-8

# # Three algorithms for integer multiplication
# 
# 
# Again we want to distinguish between the decription of a problem, the description of several solutions (in our case algorithms) and the programs that implement these algorithms. 
# 
# We also introduce two ways of exploring our programs:
# 
# 1) figuring out how to test that the program does what we want, and 
# 
# 2) figuring out how to explore what happens with execution time as the size of the input gets bigger and bigger.  
# 
# The problem is discussed in detail in the first chapter of the book [Algorithms illuminated](http://www.algorithmsilluminated.org). The website for the book includes detailed videos that explain the problem and the three solutions. In this section we focus on the programs that implement the three solutions. Our purpose is to continue to show how to go from an algorithm to a Python program. 
# 
# The problem is to calculate the product of two non negative integer numbers. This seems trivial: you know how to do this with pen and paper with what we call the school algorithm. And Python has an operation ```*``` that works perfectly well. So why bother? 
# 
# On the one hand it helps us focus on a problem that you can understand without any effort. On the other hand we hope to surprise you with a couple of solutions that seem very strange and give you a feeling for how very different solutions to the same problem might be. And finally, you will get to know one of the algorithms that are used in real systems to multiply big numbers (numbers with more than 1000 digits). Python uses this algorithm to multiply numbers larger than those that can be multiplied using the machine instruction for multiplication.
# 
# 
# ## Some programs we need
# 
# All algorithms and programs we show in this section use lists of digits. Instead of tables for multiplication and addition we use Python operations ```*``` and ```+``` when we need the result for one-digit numbers (observe that the result of adding or multiplying two one-digit numbers can be a two-digit number so we extract the two digits using ```// 10``` and ```% 10```. 
# 
# We will need addition and subtraction. The functions ```plus``` and ```minus``` implement the algorithms that we all learned at school to add and subtract numbers. Put some effort in understanding the details in different parts of each program:
# 
# * making both lists of the same size by adding 0:s to the left
# 
# * use of carry
# 
# * going trough the number from least significant digit to most significant digit.

# In[1]:


# addition for two lists of digits
def plus(m, n):
    
    # Make them the same length by adding leading 0s
    if len(m)<len(n): m = [0] * (len(n)-len(m)) + m
    if len(n)<len(m): n = [0] * (len(m)-len(n)) + n
        
    # build the list for the result
    carry  = 0
    sum    = [0] * len(m)
    
    for i in reversed(range(len(m))):
        a = m[i] + n[i] + carry # here we can get a two-digit number
        carry = a // 10
        sum[i] = a % 10

    # possibly extend it with the carry!
    if carry > 0: sum.insert(0,carry)
    return sum

# subtraction for two lists of digits m and n
# both m,n >= 0, m >= n
def minus(m,n):
    # Make them the same length by adding leading 0s
    if len(m)<len(n): m = [0] * (len(n)-len(m)) + m
    if len(n)<len(m): n = [0] * (len(m)-len(n)) + n  
        
    carry = 0
    diff = [0] * len(m)
    
    for i in reversed(range(len(m))):
        b = n[i] + carry
        if m[i] >= b: 
            diff[i] = m[i] - b
            carry = 0
        else:
            diff[i]= 10 + m[i] - b
            carry = 1
    return diff


# Here is an example. To add 123 and 45 we call the function ```plus``` with the lists ```[1,2,3]``` and ```[4,5]```: 
# ```Python
# plus([1,2,3], [4,5])
# ```
# 
# The function starts by making the lists have the same length without changing their meaning as numbers:
# 
# ```Python
# m = [1,2,3]
# n = [0,4,5]
# ```
# 
# The function initializes the carry to 0 and the list with the result to 0s:
# 
# ```Python
# carry = 0
# sum   = [0,0,0]
# ```
# 
# The function goes through all the elements of both lists from the back to the front (look at the ```reversed(range(len(m)))``` in the ```for``` loop) doing what you would do with pen-and-paper: add the two digits in a given place from the two lists, add the carry and split it into the digit you put in the result and the carry. 
# 
# ```Python
# a      = 3 + 5 + 0  # 8
# carry  = 8 // 10    # 0
# sum[2] = 8 % 10     # 8
# ```
# 
# ```Python
# a      = 2 + 4 + 0 # 6
# carry  = 6 // 10   # 0
# sum[1] = 6 % 10    # 6
# ```
# 
# ```Python 
# a      = 1 + 0 + 0 # 1
# carry  = 1 // 10   # 0
# sum[0] = 1 % 10    # 1
# ```
# 
# When this is done it might be tha case that there is a non-zero carry that has to be added at the beggining of the number. In the example this is not the case.
# 
# ### How would you test this?
# 
# In this course we will often want to understand both whether the algorithm works correctly (calculates what it should) and whether it is feasible (how does execution time grow when the size of the input grows?).
# 
# 1) For understanding whether it works correctly we can try to convert back and forth from lists of digits to numbers and compare the result of our program with Python's ```*```.
# 
# 2) For understanding how the execution time grows when the size of the input grows, we need first to understand what to consider the size of the input. What is it in the input that influences the number of operations the program has to execute?
# 
# #### To and from integers
# 
# For 1) we would like to compare the results of our operations with the operations in Python for numbers. In order to be able to use lists and numbers we define the functions ```to_int``` and ```from_int```. 
# 
# These functions should be such that for any list of digits ```n``` 
# 
# ```Python
# from_int(to_int(n)) == n 
# ```
# 
# and for any number ```n```
# 
# ```Python
# to_int(from_int(n)) == n 
# ```
# 

# In[2]:


def to_int(n):
    res = 0
    for i in range(len(n)):
        res = res + n[i] * 10**(len(n)-i-1)
    return res

def from_int(n):
    if n < 10: return [n]
    return from_int(n // 10) + [n % 10]


# In[3]:


to_int([1,2,3])


# In[4]:


from_int(45)


# With these two functions we can program a function to test our plus function:

# In[5]:


def test_plus(m, n):
    return to_int(plus(m,n)) == to_int(m) + to_int(n)


# In[6]:


test_plus([1,2,3],[4,5])


# We can in fact program a function that generates random lists of digits and does this test. 
# 
# The argument to this new function is the number of times we want to run our test.

# In[7]:


import random


# In[8]:


def test_plus_random(times):
    for i in range(times):
        
        # generate 2 random non negative numbers
        a = random.randrange(0,1000)
        b = random.randrange(0,1000)
        
        # calculate their lists of digits
        m = from_int(a)
        n = from_int(b)
        
        # test whether the function plus of the two lists 
        # produces a different value than Python's +
        # if this is the case we do not neeed to test any more:
        # produce an error message and return False
        if a + b != to_int(plus(m,n)):
            print(m, 'plus', n, '=', plus(m,n), 'but should be', a + b,'.')
            return False
        
    # If the program gets here (observe: the for loop has terminated!)
    # we know that there were no cases that produced the wrong result!
    # print a message and return True
    print('Passed all', times, 'test cases.')
    return True


# In[9]:


test_plus_random(100)


# In[10]:


def test_minus_random(times):
    
    for i in range(times):
        
        # generate 2 random numbers, first one bigger
        a = random.randrange(100,1000)
        b = random.randrange(0,100)
        
        # calculate their lists of digits
        m = from_int(a)
        n = from_int(b)
        
        # test whether the function minus
        # produces a different value than Python's -
        # if this is the case we do not neeed to test any more:
        # produce an error message and return False
        if a-b != to_int(minus(m,n)):
            print(m, 'minus', n, '=', minus(m,n), 'but should be', a-b,'.')
            return False
        
    # If the program gets here (observe: the for loop has terminated!)
    # we know that there were no cases that produced the wrong result!
    # print a message and return True
    print('Passed all', times, 'test cases.')
    return True


# In[11]:


test_minus_random(100)


# The code for these two functions is very (**very**) similar! The only difference is that we use either ```plus```or ```minus``` and ```+``` or ```-```! 
# 
# Fortunatelly in Python we can use functions as arguments to other functions. Then we can program the following testing function:
# 

# In[12]:


def test_fun_random(times, function_under_test, reference_function):
    
    for i in range(times):
        
        a = random.randrange(1000,2000)
        b = random.randrange(0,1000)
        
        m = from_int(a)
        n = from_int(b)
        
        if reference_function(a, b) != to_int(function_under_test(m,n)):
            print('correct result is', reference_function(a,b), 'but found', function_under_test(m,n))
            return False
        
        
    print('Passed all', times, 'test cases.')
    return True


# In order to use arithmetic operators as functions we need to use the module ```operator``` from Python where all operators have an associated function: [Standard operators as functions](https://docs.python.org/3/library/operator.html)

# In[13]:


import operator


# In[14]:


# The function under test is plus and the reference function is + (used as operator.add)
test_fun_random(100, plus, operator.add)


# In[15]:


# The function under test is minus and the reference function is - (used as operator.add)
test_fun_random(100, minus, operator.sub)


# 
# ## The school algorithm for multiplication
# 
# The first solution to the problem of computing the product of two non negative integers is the algorithm most of us learned at school and that Tim Roughgarden discusses in the book and in one of the videos. 
# 
# Here we illustrate it with an example:
# ```Python
#    1234
#    x 56
# --------
#    7404
#   61700
# --------
#   69104
# ```
# where 
# ```Python
# 7404 == 1234 * 6
# ```
# 
# ```Python
# 6170 == 1234 * 5
# ```
# 
# and 
# ```Python
# 69104 == 7404 + 61700
# ```
#   
# We already know how to add two lists of digits, we now need a program to multipy a digit and a list of digits.

# In[16]:


def digit_times_number(d,n):

    # build the list for the result
    carry  = 0
    result = [0] * len(n)
    
    for i in reversed(range(len(n))):
        a = d * n[i] + carry # here we can get a two-digit number
        result[i] = a % 10
        carry = a // 10
    
    # possibly extend it with the carry!
    if carry > 0: result.insert(0,carry)
    return result


# In[17]:


digit_times_number(6,[1,2,3,4])


# In[18]:


digit_times_number(5,[1,2,3,4])


# With this we can implement the school algorithm for multiplication:

# In[19]:


def school_mul(m, n):
    lines = [None] * len(n)
    for i in reversed(range(len(n))):
        lines[i] = digit_times_number(n[i],m) + [0]*(len(n)-1-i)
       
    sum = []
    for line in lines:
        sum = plus(sum, line)
    return sum


# In[20]:


school_mul([1,2,3,4], [5,6])


# ### How would you test this?
# 
# Again we need to convince ourselves that the program works. Fortunately we have a function that helps already!

# In[21]:


test_fun_random(100, school_mul, operator.mul)


# What is the input to our program ```school_mul```? 
# 
# *Two lists of digits.*
#     
# What aspect of the input affects the number of operations done to calculate the result?
# 
# *The number of elements in the longest list determines how many turns of the loops are needed. This is what decides how many operations are needed.*
#     
# This is what we call *the size of the input*.
# 
# We are interested on understanding the execution time as a function of the size of the input. There are theoretical methods for doing so but we can already now do experiments with our program. Here is a systematic experiment:
# 
# * run the program several times with input of a given size meassuring the execution time and taking the average
# 
# * double the size of the input and do the same
# 
# * double again and do the same
# 
# * do this several times
# 
# And now? Well we can plot execution time versus size of input, but it can be difficult to see what function this is. If we assume that it will be a function of the form $time = size ^n$ for some $n$, we need to find this $n$! There is a method for doing this and it is to calculate **the slope** of $\log(time)$ as a function of $\log(size)$.
# 
# In order to meassure execution time, there are functions in Python to get timestamps from the system in the library ```time``` that we need to import. Here are some useful functions, all of which are meant to be used to calculate differences between to instants:
# 
# ```time.process_time_ns()``` returns an integer: the sum of the system and user CPU time of the current process. It does not include time elapsed during sleep. It is process-wide by definition. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.
# 
# ```time.perf_counter_ns()``` returns an integer: the value of a performance counter, i.e. a clock with the highest available resolution to measure a short duration. It does include time elapsed during sleep and is system-wide. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.
# 
# ```time.time_ns()```  returns time as an integer number of nanoseconds since the epoch.
# 
# We will meassure execution time using  ```time.process_time_ns()``` in the following way:
# 
# ```Python
# start = time.process_time_ns()
# school_mul(m,n)
# execution_time = time.process_time_ns() - start
# ```
# 
# Here is an example. Try it several times, you will see that you do not get always the same result. This is related to the fact that there other programs running in your computer. We deal with this by repeating the experiment and taking an average.

# In[22]:


import time


# In[23]:


m = list(range(100))
n = list(range(100,200))
start = time.process_time_ns()
school_mul(m,n)
time.process_time_ns() - start


# We define a function for testing execution time of functions that can be applied to two lists of digits (for example ```plus```, ```minus``` and ```school_mul```). 

# In[24]:


# The argument size is for the length of the list of digits
# The argument times is for the number of times to repeat the experiment
def test_et(size, times, f):
    m = list(range(size))
    n = list(range(size,2*size))  
    sum = 0
    for i in range(times):
        start = time.process_time_ns()
        f(m,n)
        sum += time.process_time_ns() - start
    return sum / times


# In[25]:


# 100 experiments with numbers of 10 digits
test_et(10,100, school_mul)


# Can you say something about how execution time grows as the size of the input grows? 
# 
# Something like 
# 
# *when the size of the input doubles (gets multiplied by 2) the execution time gets multiplied by ...*
# 
# ## A recursive algorithm
# 
# And now we look at a completely different algorithm. To begin with, just believe in it! 
# 
# We recommend that you read the book where the algorithm is explained. Here is the program in Python.

# In[26]:


def rec_mul(m,n):
    if len(m) == 1: return digit_times_number(m[0], n)
    if len(n) == 1: return digit_times_number(n[0], m)
    
    # Make them the same length by adding leading 0s
    if len(m)<len(n): m = [0] * (len(n)-len(m)) + m
    if len(n)<len(m): n = [0] * (len(m)-len(n)) + n

    mid = len(m) // 2
    
    a = m[0:mid] # the first half of m
    b = m[mid:]  # the second half of m
     
    c = n[0:mid] # the first half of n
    d = n[mid:]  # the second half of n
    
    # turning mid into the power of 2 we need.
    if len(m) % 2 == 1: mid+=1
       
    # Four recursive calls with lists shorter than m and n!
    z0 = rec_mul(a,c) + 2 * mid * [0] 
    z1 = rec_mul(a,d) + mid * [0] 
    z2 = rec_mul(c,b) + mid * [0] 
    z3 = rec_mul(b,d)  
    
    return plus(z0, plus(z1, plus(z2,z3)))


# In[27]:


test_fun_random(100, rec_mul, operator.mul)


# In[28]:


test_et(10,100,rec_mul)


# ## Karatsuba's algorithm
# 
# Finally, a great insight is that one recursive calls can be eliminated! 

# In[29]:


def karatsuba_mul(m,n):
    if len(m) == 1: return digit_times_number(m[0], n)
    if len(n) == 1: return digit_times_number(n[0], m)

    # Make them the same length by adding leading 0s
    if len(m)<len(n): m = [0] * (len(n)-len(m)) + m
    if len(n)<len(m): n = [0] * (len(m)-len(n)) + n

    mid = len(m) // 2
    
    a = m[0:mid]
    b = m[mid:]
    c = n[0:mid]
    d = n[mid:]
    
    # turning mid into the right power of 2.
    if len(m) % 2 == 1: mid+=1
        
    z0 = karatsuba_mul(b,d)
    z1 = karatsuba_mul(plus(b,a), plus(d,c)) 
    z2 = karatsuba_mul(a,c)  
    p = minus(minus(z1, z2),z0)

    return plus(z2 + 2 * mid * [0], plus(p + mid * [0],z0))


# In[30]:


test_fun_random(100, karatsuba_mul, operator.mul)


# In[31]:


test_et(10,100,karatsuba_mul)


# You should use the next cell to experiment with small numbers (100 digits) and big numbers (2000 digits). 
# 
# As it is it will take some time: it meassures the execution time of Karatsuba's multiplication for numbers with 2048 digits, meassures the execution time of the school algorithm for numbers with 3000 digits and takes their quotient.

# In[32]:


test_et(2048,1, karatsuba_mul) / test_et(2048,1, school_mul) 


# So it seems that for short numbers, school multiplication is better. lets try to combine them by cutting off recursion before getting to 1 digit.

# In[33]:


def karatsuba_mul_cutoff(m,n):
    
    if len(m) < 10 and len(n) < 10: return school_mul(m,n)

    # Make them the same length by adding leading 0s
    if len(m)<len(n): m = [0] * (len(n)-len(m)) + m
    if len(n)<len(m): n = [0] * (len(m)-len(n)) + n

    mid = len(m) // 2
    
    a = m[0:mid]
    b = m[mid:]
    c = n[0:mid]
    d = n[mid:]
    
    # turning mid into the right power of 2.
    if len(m) % 2 == 1: mid+=1
        
    z0 = karatsuba_mul_cutoff(b,d)
    z1 = karatsuba_mul_cutoff(plus(b,a), plus(d,c)) 
    z2 = karatsuba_mul_cutoff(a,c)  
    p = minus(minus(z1, z2),z0)

    return plus(z2 + 2 * mid * [0], plus(p + mid * [0],z0))


# In[34]:


test_fun_random(100, karatsuba_mul_cutoff, operator.mul)


# In[35]:


test_et(1000,1,karatsuba_mul_cutoff) / test_et(1000,1,school_mul) 


# In[36]:


print(test_et(2000,1,karatsuba_mul_cutoff) )
print(test_et(2000,1,school_mul))


# In[37]:


# test case from the book Algorithms illuminated
e  = 2718281828459045235360287471352662497757247093699959574966967627
pi = 3141592653589793238462643383279502884197169399375105820974944592 

el  = from_int(e)
pil = from_int(pi)

print(karatsuba_mul(el,pil))
print(e*pi)

