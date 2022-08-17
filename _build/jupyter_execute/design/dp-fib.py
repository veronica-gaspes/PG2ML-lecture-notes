#!/usr/bin/env python
# coding: utf-8

# # Fibonacci numbers
# We look at this example first because it helps illustrate a problem that might arise in recursive programs: that the recursive calls are overlapping and require re-calculations that make the program infeasible. This has not been the case in the examples we have seen of recursive programs arising from Divide & Conquer.
# 
# Dynamic programming is a way of dealing with programs that appear to use solutions to overlapping subproblems. 
# 
# The series of Fibonacci numbers is 
# ```Python
# 1 1 2 3 5 8 13 21 34 55 ...
# ```
# You obtain the next term by adding the two previous terms. The numbers in the series grow very fast. The series is intriguing, there are many relations between the numbers in the series and between the series  and natural phenomena. Check the Wikipedia entry [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
# 
# Here is a program that helps you calculate the n-th term of the series where we assume the *index* starts from 0:

# In[1]:


def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)


# In[2]:


[fib(i) for i in range(10)]


# Of course we want to use our program to calculate numbers higher up in the sequence. For example, what is the 100-th Fibonacci number? 
# 
# Don't even try it! In my system it is already difficult to get an answer for ```fib(40)```!

# In[3]:


fib(20)


# In order to see what the issue is, here is a version of the same function that prints the argument with which it is called:

# In[4]:


def fib_print_argument(n, level):
    indent = '-' * level
    print(indent, n)
    if n < 2: 
        return 1
    return fib_print_argument(n-1, level + 1) + fib_print_argument(n-2,level + 1)


# In[5]:


fib_print_argument(5, 0)


# You can see that the computation ```fib(3)``` is done twice. 
# 
# Now check 

# In[6]:


fib_print_argument(6,0)


# The whole computation for ```fib(4)``` is done twice. And we see that the computation of ```fib(3)``` is repeated in its entirety 3 times! 
# 
# Finally, check ```fib(10)``` and try to relate it to ```fib(5)```:

# In[7]:


fib_print_argument(10,0)


# The issue is that computations are done over and over again. The *subproblems*  are overlapping: ```fib(n-2)``` is part of the computation of ```fib(n-1)```, but we ask for it to be done again to solve ```fib(n)```.
# 
# Lets now look at the three components of Dynamic programming and see how we can use them in this case:
# 
# 
#  1) Identify a relatively small number of subproblems.
#  
#  2) Show how to quickly and correctly solve *larger* problems given solutions to *smaller* problems.
#   
#  3) Show how to quickly and correctly infer the final solution from the solutions to all the subproblems. 
#  
# The algorithm you obtain is to systematically solve all the subproblems one by one, working from smallest to largest and extract the final solution from the solutions to the subproblems. 
#     
# 
# For step 1) given that we want to compute Fibonacci number $n$ we choose *two* smaller problems $n-1$ and $n-2$
# 
# For step 2) given solutions to smaller problems $n-1$ and $n-2$ we just need to add them to form a solution to the larger problem $n$.
# 
# For step 3) given solutions to *all smaller problems* (all sizes $0$ upto $n$), just pick the last one!
# 
# The algorithm is then to start with the first two small problems for $0$ and $1$ and then calculate for $2$, then for $3$ and so on until we get to calculate for $n$. We can do this using an array:

# In[8]:


def dp_fib(n):
    if n < 2: return 1
    
    all_smaller = [0] * (n + 1)
    all_smaller[0] = 1
    all_smaller[1] = 1
    for i in range(2, n + 1):
        all_smaller[i] = all_smaller[i-1] + all_smaller[i-2]
    return all_smaller[-1]
    
    


# In[9]:


[dp_fib(i) for i in range(10)]


# In[10]:


dp_fib(100)


# We solved all smaller problems, but we solved them only one time each! Now we can compute large Fibonacci numbers! Try 1000, it takes less than the blink of an eye. 
# 
# *Can we do better?* Well yes: we store all solutions, but to compute the next number we only use two. We might as well use 2 variables instead of the array!

# In[11]:


def better_dp_fib(n):
    if n < 2: return 1
    
    fib_1 = 1 # for fib(n-1)
    fib_2 = 1 # for fib(n-2)
    
    for i in range(2, n + 1):
        fib   = fib_1 + fib_2
        
        fib_2 = fib_1
        fib_1 = fib
        
    return fib
        


# In[12]:


[better_dp_fib(i) for i in range(10)]


# In[13]:


better_dp_fib(1000)


# In[ ]:




