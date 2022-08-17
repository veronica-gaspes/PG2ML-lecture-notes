#!/usr/bin/env python
# coding: utf-8

# # Solutions to programming exercises 1
# 
# These exercises relate to the first lecture where we showed 2 problems, several algorithms for each problem and several programs for each algorithm.
# 
# The problems from the lecture were:
# 
# 1) Calculate all prime numbers smaller or equal to a given bound
# 
# 2) Calculate the product of two non negative integers
# 
# The lecture also included brief introductions to ```for``` loops and recursion.
# 
# ## Exercises
# 
# 1) Program a recursive function to convert a number to base 16 (hexadecimal). Use strings 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F for the figures. For example, number 15 should be converted to ```'F'``` and number 16 to ```'10'```. Complete the code in the following cell where indicated.

# In[1]:


figures = '0123456789ABCDEF'
def hexadecimal(n):
    # Your code here.
    # use an if-statement to distinguish the base case from the recursive case.
    # use the definition of binary from the lecture as inspiration
    if n < 16: return figures[n]
    else: return hexadecimal(n // 16) + figures[n % 16]
        


# 2) Program a function to test your implementation. 
# 
#     a) Define a function that takes a string describing a hexadecimal number and calculates the integer value of it (we provide you with the definition below, see ```from_hexa```). 
#     
#     b) Define a function that generates random numbers and then tests equality of the number generated with the number obataines by first converting to hexadecimal and then back to number. 

# In[2]:


import random


# In[3]:


def from_hexa(h):
    res = 0
    for i in range(len(h)):
        res = res + figures.find(h[i]) * 16**(len(h)-i-1)
    return res
    
def test_hexadecimal(times):
    # Your code here
    # times is the numbers of experiments your function should do
    for i in range(times):
        n = random.randrange(1000)
        m = hexadecimal(n)
        if n != from_hexa(m):
            print(n, 'was converted to', m, 'but this is not correct')
            return False
    print('Passed all', times, 'tests.')
    return True


# In[4]:


test_hexadecimal(100)


# 3) Modify your function ```hexadecimal``` so that it returns a pair: the hexadecimal string for the argument and the number of recursive calls. Complete the code in the function ```hexadecimal_count``` below. 

# In[5]:


def hexadecimal_count(n, c):
    # Your code here
    # You will call the function with 0 for c.
    # The return value is a pair, you need to handle this to build the hexadecimal string
    if n < 16: return (figures[n], c)
    else: 
        (h, ct) = hexadecimal_count(n // 16, c)
        return (h + figures[n % 16], ct+1)


# In[6]:


hexadecimal_count(16*16*16*16,0)


# 
# 4) Use your function to complete in the following table
# 
# | n  |  count recursive calls |
# ----: | :----:
# | 10 |   0 |
# | 100 |   1 |
# | 1000 |    |
# | 10000 |    |
# | 100000|    |
# | 1000000|    |
# | 10000000|  |
# | 100000000 | |
# 
# What **grows** faster? The input n or the number of recursive calls? 
# 

# In[ ]:




