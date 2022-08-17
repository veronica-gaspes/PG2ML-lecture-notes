#!/usr/bin/env python
# coding: utf-8

# # Understanding recursion
# 
# Recursion is about using what you are defining in the definition! You have to be careful so that using the defintion does not get the program in an infinite computation (but this is not unique for recursion, also loops can engage in an infinite computation if you are not careful).
# 
# We start with an example. 
# 
# You already know that the last digit of a number is the remainder of integer division with 10.
# 
# You also know that you can remove the last digit by taking the quotient of integer division with 10.

# In[1]:


print(123456789 % 10)
print(123456789 // 10)


# How does this look for numbers with only one digit?

# In[2]:


print(9 % 10)
print(9 // 10)


# So, how can we calculate the list of digits? 
# 
# Well, we can use the remainder trick on each of the numbers we obtain using the quotient and put these in a list.
# 
# Something like 
# 
# *the list of digits for 123456789* is *the list of digits for 12345678* with one more element: *9*!
# 
# If we define a function ```digits(n)``` to return the list we would like 
# 
# ```
# digits(123456789) == [1,2,3,4,5,6,7,8,9] 
#                   == [1,2,3,4,5,6,7,8] + [9] 
#                   == digits(123456789 // 10) + [123456789 % 10]
# ```
# 
# We would then want the definition to be
# ```Python
# 
# def digits(n):
#     return digits(n // 10) + [n % 10]
#      
# ```
# 
# The problem is that we then get 
# 
# ```Python
# digits(123) 
# ==
# digits(12) + [3]
# ==
# (digits(1) + [2]) + [3]
# ==
# ((digits(0) + [1]) + [2]) + [3]
# ==
# digits(0) + 0 + [1] + [2] + [3]
# ==
# digits(0) + 0 + 0 + [1] + [2] + [3]
# ...
# 
# ```
# An infinite computation!
# 
# This can be avoided using return to stop computation as soon as the argument needs not be divided any more: the number is a digit (easy to detect: smaller than 10!).

# In[3]:


def digits(n):
    if n < 10: return [n]
    return digits(n // 10) + [n % 10]
     


# In[4]:


digits(123456789)


# Of course there are other ways of solving the same problem. Here are some.

# In[5]:


def digits1(n):
    return [int(d) for d in str(n)]


digits1(123456789)


# In[6]:


def digits2(n):
    d = n % 10
    n = n // 10
    res = [d]
    while n > 0:
        d = n % 10 
        n = n // 10
        res = [d] + res 
    return res


digits2(123456789)


# Recursion is very useful, and in many cases recursive solutions are the most efficient ones. We will see examples of this when we discuss a technique for comming up with algorithms called Divide & Conquer.
# 
# Now we present some more examples so that you get used to read programs that use recursion.
# 
# Three ideas are important:
# 
# * You need one or more *base cases* (return the result without calling the function you are defining).
# 
# * The *recursive calls* have to be made with arguments that get you closer to one of the base cases.
# 
# * You have to trust the recursive call!
# 
# We explore these in the following examples.
# 
# ## Example 1: Converting a number to another base
# Literals for integer numbers in Python are digits (0 to 9, decimal system, base 10). In math we can use literals in other bases. In a programming language we can at least build strings if we want to see how the literal for a given number would be in another base. 
# 
# We start with base 2, using 0 and 1 only and powers of 2 (instead of 10) for the positional system. Here is a function to produce a string with 0s and 1s in the right positions to represent a binary literal. Observe that the argument is an integer number but the result is a string.
# 
# * The base case is for when we can outright calculate the binary representation of a number: when it is either 0 or 1!
# 
# * There is only one recursive call, with ```n // 2```. This number is smaller than ```n``` for ```n > 0```.
# 
# * If we trust that ```binary``` works, then ```binary(n // 2)``` is a list with 0s and 1s for the binary representation of ```n // 2```. In order to get the representation for ```n```we have to add a 0 or a 1 depending on whether n is even or odd: we add ```n % 2```.

# In[7]:


def binary(n): 
    if n < 2: return str(n)
    return binary(n // 2) + str(n % 2)


# In[8]:


[binary(k) for k in range(10)]


# ## Quiz
# 
# Why did we not use ```else``` before the recursive call?
# 
# ## Quiz
# 
# Can you extend the definition so that it works for negative numbers?
# 
# ## Quiz
# 
# How would you define the conversion to base 16 (hexadecimal)? For one thing, you need to use more *digits* in your strings: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F. What are the base cases? Try a Python definition!
# 
# ## Example 2: Towers of Hanoi
# 
# The following example uses recursion to solve the [Towers of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle. 
# 
# The puzzle has three pegs or rods and some disks of different diameters. To begin with the disks are all in one peg, ordered from largest diameter (at the bottom) to smallest diameter (at the top). In the puzzle you are asked to move all disks to another peg, one by one, never placing a larger disk on top of a smaller disk. 
# 
# The following link is an animation that illustrates how it works for 6 disks: 
# https://en.wikipedia.org/wiki/Tower_of_Hanoi#/media/File:Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif 
# 
# We want a program that tells us how to move the disks at each step. 
# 
# The program takes a number (how many disks to use) and names the pegs using numbers or letters. The result is an instruction of how to proceed: take the top disk from a peg and put on another peg!
# 
# Say that the pegs are named A, B and C. Say that there are n disks placed on A that we want to move to B using C to help.
# 
# If we could solve the problem moving n-1 disks from A to C using B to help, then we could move the largest disk to B without breaking any rule! Finally we could move the n-1 disks from C to B using A to help!
# 
# 

# In[9]:


def hanoi(n, a, b, c):
    if n == 0: return
    if n == 1: 
        print(a, '->', b)
        return
    if n > 1:
        hanoi(n-1, a, c, b)
        print(a, '->', b)
        hanoi(n-1, c, b, a)


# In[10]:


hanoi(4, 'A','B','C')


# ## Quiz
# 
# Can you modify the program to count how many moves you need?
# 
# ### Answer:

# In[11]:


def hanoi_count(n):
    if n == 0: return 0
    if n == 1: return 1
    if n > 1:
        c1 = hanoi_count(n-1)
        c2 = hanoi_count(n-1)
        return c1 + 1 + c2 # all the moves for n-1, plus 1 move, plus all the moves for n-1


# In[12]:


hanoi_count(10)


# Now try to use it! You can see that it takes a lot of moves! For 10 disks we need 1023 moves! If you try to calculate the number of moves for 30 disks you might have to wait a lot! Imagine also doing the moves!
# 
# We cannot remove the recursive calls from ```hanoi``` but we can do with only one recursive call for counting! And then we can calculate the number of moves for larger values of n (try 100).

# In[13]:


def hanoi_count_better(n):
    if n == 0: return 0
    if n == 1: return 1
    if n > 1:
        return 2 * hanoi_count_better(n-1) + 1


# In[14]:


hanoi_count_better(100)

