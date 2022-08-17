#!/usr/bin/env python
# coding: utf-8

# # Order and sorting
# 
# The book Algorithms illuminated swiflty describes three solutions to the sorting problem in less than a page. The three solutions are discarded immediatelly because *they all have quadratic running times*.
# 
# We walk you through how the Python operator ```<``` works for different types, we implement the three algorithms just mentioned and we briefly show howcome *they all have quadratic running times* and why this means that they have to be discared.
# 
# ## The ```<``` operator in Python
# 
# This operator works as expected for integers. Here is an example with 3 cases:

# In[1]:


(1 < 2, 1 < 1, 2 < 1)


# But what about strings, tuples and arrays? In all these cases it works as alphabetical ordering. Here are some examples with strings where it is clear that it is the first character that decides and only in case of having the same first character it is the second character that decides and so on.

# In[2]:


print(''   < 'a')
print('a'  < 'aa')
print('az' < 'b')
print('ab' < 'az')
print('ab' < 'aa')
print('b'  < 'abbbb')


# The same holds for arrays and tuples. Here are the same examples for arrays:

# In[3]:


print([]     < [1])
print([1]    < [1,1])
print([1,99] < [2])
print([1,2]  < [1,99])
print([1,2]  < [1,1])
print([2]    < [1,2,2,2,2])


# And finally some examples for tuples, that we treat differently given that tuples typically have elements of different types.

# In[4]:


print((1,'a') < (2, 'a'))
print((1,'a') < (1, 'a'))
print((1,'a') < (1, 'b'))


# ## Sorting arrays
# 
# The problem can be (informally) described as: 
# 
# Given an array as input, produce an array as output that has the same elements but in order (from smaller to larger).
# 
# ### Sorting arrays in Python
# 
# Python provides a function and a method that solve the problem of sorting arrays in different ways:
# 
# 1) The function ```sorted``` can be used to form an expression: it calculates a value, an array that is sorted, without modifying the argument. The function is used as in ```sorted([1,3,2])```. This expression has value ```[1,2,3]```. We can say that the input is the argument to the function and the output is the result of applying the function.
# 
# 2) The method ```sort``` can be used to form a statement (a command): it has an effect, sorting an array, without producing any value. The method is used as ```a.sort()``` and ```a``` becomes sorted when this command is used. We can say that the input is ```a``` and the output is also ```a```. 
# 
# The following four cells illustrate this

# In[5]:


sorted([1,3,2])


# In[6]:


# This cell shows that sorted(a) is a sorted list and that a does not change.
a = [1,3,2]
print(sorted(a))
print(a)


# In[7]:


# This cell shows that sort() does not calculate a value.
[1,3,2].sort()


# In[8]:


# This cell shows that sort modifies the list a.
a = [1,3,2]
a.sort()
a


# The three solutions to sorting lists presented swifly in the book and then discarded because of their running time behavious are easy to program. We do so in order to compare the running time behaviour of all solutions. 
# 
# To help you understand the programs you can check the animations at [ComparisonSort](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) by professor [David Galles](https://www.cs.usfca.edu/~galles/)
# 
# ### Selection sort
# 
# Here is how the book [Algorithms illuminated](https://algorithmsilluminated.org) describes this algorithm:
# 
# *First scan the input array to identify the minimum element and copy it over to the first element of the output array; then do another scan to identify and copy the second-smallest element; and so on.*
# 
# What follows is a program that implements this algorithm using the same array as input and output. In order not to loose the element that gets overwritten by the least element we swap elements.
# 
# In order to scan the input to identify the minimum element we define a function to return the position of the minimum element in an array. The function that sorts calls this function repeatedly with shorter and shorter suffixes of the original array.

# In[9]:


def min_pos(a):
    mp = 0
    for i in range(len(a)):
        if a[i] < a[mp]: mp = i
    return mp

    
def selection_sort(a):
    n = len(a)
    for i in range(n):
        j = i + min_pos(a[i:n])
        a[i],a[j] = a[j],a[i]    


# In[10]:


a = [1,3,2]
selection_sort(a)
a


# ### Insertion sort
# 
# Keep the prefix sorted and extend the prefix: grow a sorted prefix of the array. The implementation looks at the next element and moves it to its position among the previous elements in the array. 
# 

# In[11]:


def insertion_sort(a): 
    for i in range(1,len(a)):
        j = i
        while(j > 0 and a[j] < a[j-1]):
            a[j],a[j-1] = a[j-1],a[j]
            j = j - 1                   


# In[12]:


a = [3,1,2]
insertion_sort(a)
a


# ## How can we test these programs?
# 
# We can use the function that calculates a sorted version of an array and compare its result with the modified array our functions create.
# 
# In the function ```test_sorting_program_once``` the argument ```p``` is the program to be tested and the argument ```a``` is the array to be sorted.

# In[13]:


def test_sorting_program_once(p, a):
    b = sorted(a)
    p(a)
    if b != a: print('expected', b, 'but found', a)
    return a == b


# In[14]:


test_sorting_program_once(insertion_sort, [1,3,2])


# And now we want to  be able to do several random tests. We need to generate random lists.
# 
# So, how do we generate random lists? 
# 
# If we focus on lists of numbers we can think of providing a lower and an upper bound for the numbers that can appear in the list and a lower and an upper bound for the lenght of the list.
# 
# Here is a possibility:

# In[15]:


import random


# In[16]:


def random_number_list(lower,upper,short,long):
    length = random.randrange(short,long)
    return [random.randrange(lower,upper) for i in range(length)]


# In[17]:


# 10 lists of numbers between -10 and 10 with lengths 0 to 4
[
    random_number_list(-10,10, 0, 5) 
    for i in range(10)
]


# In[18]:


# 10 lists of numbers between -10 and 10 all of length 5
[
    random_number_list(-10,10, 5, 6) 
    for i in range(10)
]


# So, now we can program a function to test our sorting programs:

# In[19]:


def test_sorting_program(p, times):
    for i in range(times):
        if not test_sorting_program_once(p, random_number_list(-10,10,0,1000)):
            return False
    return True
        


# In[20]:


test_sorting_program(insertion_sort, 100)


# In[21]:


test_sorting_program(selection_sort, 100)


# ### The execution time
# 
# We are now more or less convinced that our programs solve the problem of sorting lists. 
# 
# Before moving on how to study running time behaviour of algorithms we use some experiments to expose you to how running time becomes *visible*.
# 
# Try the following code with increasing values of ```size```. Try 1000, 2000, 4000, 8000, 16000. 
# 
# Try describing what you experience. 
# 
# It is this running time behaviour that makes these algorithms not usable in practice. 

# In[22]:


size = 100
a = list(reversed(range(size)))
b = list(reversed(range(size)))
c = list(reversed(range(size)))

print('start')
a.sort()
print('sort done')
selection_sort(b)
print('selection_sort done')
insertion_sort(c)
print('insertion_sort done')


# ## An exercise
# 
# Now you have seen how to write programs for two of the three algorithms described in the book that were discarded because ot their running time behaviour. The third one, known as bubble sort, is left as an exercise. Make sure you program it, you test it using ```test_sort_program``` and you experiment with its execution time by adding it to the list of sorting algorithms in the previous cell where you increment ```size```. 

# In[23]:


def bubble_sort(a):
    # your code here
    pass # you can remove this line

