#!/usr/bin/env python
# coding: utf-8

# # Hash tables
# 
# Hash tables are discussed in sections 12.1 to 12.4 in part 2 of the book [Algorithms Illuminated](http://www.algorithmsilluminated.org) (there are videos in the website).
# 
# Try the following code cell that uses the type ```dict```: we can use it almost as an array but where the indices are (almost) of any type! We call these indices the *keys* and the content the *values*. In other words, we use hash tables to store key-value pairs. Amazingly, the Big-O for adding elements, looking up and removing elements is $O(1)$!
# 
# phoneNumbers = dict()
# phoneNumbers['vero'] = 123
# phoneNumbers['martin'] = 456
# phoneNumbers['tim'] = 789
# 
# print(phoneNumbers['martin'])
# 
# if  'anna' in phoneNumbers: 
#     print(phoneNumbers['anna'])
# else: 
#     phoneNumbers['anna'] = phoneNumbers['tim']
#     print(phoneNumbers['anna'])
# 
# for key in phoneNumbers:
#     print (key, phoneNumbers[key])

# In[1]:


phoneNumbers = dict()
phoneNumbers['vero'] = 123
phoneNumbers['martin'] = 456
phoneNumbers['tim'] = 789

print(phoneNumbers['martin'])

if  'anna' in phoneNumbers: 
    print(phoneNumbers['anna'])
else: 
    phoneNumbers['anna'] = phoneNumbers['tim']
    print(phoneNumbers['anna'])

for key in phoneNumbers:
    print (key, phoneNumbers[key])


# The first line creates an empty dictionary. The next three lines add the pairs ```('vero', 123)```, ```('martin', 456)``` and ```('tim', 789)```.
# 
# The line ```'anna' in phoneNumbers``` tests whether there is a pair with key ```'anna'``` in the dictionary.  
# 
# Please observe that the ```for```-loop that goes through all of the keys does not get them in any specific order (if we needed to preserve an order between the elements we would use another type, implemented using binary search trees).
# 
# ## Example 1: de-duplicate
# For the first example in the book of using hash tables (de-duplicate) we write a program that removes duplicate words from a file.  In this program we use the type ```set``` in Python: uses a hash table to store values, not necessarily key-value pairs. 
# 
# In a set there is only one occurrence of each value. The operations on sets include adding an element to a set (```s.add(e)``` to add element ```e``` to the set ```s```). Adding an element that is already there has no effect!
# 
# In order to test it with a file of a reasonable size you might want to download [Tom Sawyer](https://introcs.cs.princeton.edu/python/33design/tomsawyer.txt) to the directory where you have this notebook.
# 
# 

# In[2]:


import re


# In[3]:


def de_duplicate(input_file, output_file):

    f = open(input_file, 'r')
    

    txt  = f.read()
    f.close()
    
    text = re.findall(r"[a-zA-Z']+", txt)
    
    # Now to the algorithm: just insert words in the set 
    # (implemented with a hash table!)
    words = set()
    for word in text:
        words.add(word.lower()) 
    
    # open a file for writing
    f = open(output_file,'w')
    
    # write one word at a time
    for word in words:
        f.write(word + '\n')
        
    f.close()
    
    return len(words)


# ## Quiz
# 
# If you know that the operation of adding an element to a set is $O(1)$, and the operation for retrieving an element from the set (as in the iterator in the ```for```-loop) is $O(1)$, what is the Big-O for the execution time of this program?
# 
# Again, using the right data structure makes an algorithm easy to understand and efficient!
# 
# 
# ## Example 2: count words
# 
# We expand on this example by using ```dict``` instead of ```set```: this allows us to use the words as keys and to each key associate a value to count how many times each distinct word occurrs in a file. 
# 
# 

# In[4]:


def word_count(input_file, output_file):
 
    f = open(input_file, 'r')
    txt  = f.read()
    f.close()
 
    text = re.findall(r"[a-zA-Z']+", txt)
    
    counts = dict()
    for word in text:
        w = word.lower()
        if w in counts: 
            counts[w] += 1
        else:
            counts[w] = 1
    
    f = open(output_file,'w')
    
    for word in counts:
        f.write(word + ' '+ str(counts[word]) + '\n')

    f.close()
    return len(counts)


# ## Example 3: the 2-sum problem
# 
# The next example is the 2-sum problem. In the book you can find three algorithms. The last one uses a hash table. We write programs for the three of them and use a Python ```set``` for the hash table.

# In[5]:


# brute force 2 Sum: Are there two elements x and y in a s.t. x + y = t?
# The programmer has not taken a course on algorithms and datastructures
# and does not know better!
# We signal that there is no pair that adds to t
# by returning -1 (for an index that is not possible)

def bf_2_sum(a, t):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == t: return (i, j)
    return (-1,-1)


# In[6]:


# sort and search (using binary search) to look for t - a[i]
# The programmer knows that 
# sorting can be O(n log(n)) and binary search O(log(n))!

def _bs(a, lo, hi, x):
    if hi - lo < 0: return -1
    mid = (lo + hi) // 2
    if a[mid] == x: return mid
    if a[mid] < x : return _bs(a, mid + 1, hi, x)
    return _bs(a, lo, mid - 1 , x)


def s_and_s_2_sum(a, t):
    # sorting with Pythons algorithm is O(n log(n))
    b = sorted(a)

    # n iterations and in each iteration log(n) work: O(n log(n))
    for i in range(len(a)):
        j = _bs(b, i + 1, len(b) - 1, t - b[i])
        if j != -1: return (i, j)
    return (-1,-1)


# In[7]:


# Using a hash table.
# The programmer knows that 
# inserting and looking up in a hash table is constant time!
def ht_2_sum(a, t):
    h = dict()
    # do not be confused, h is not an array. It is a hash table!
    # for duplicate elements we replace the index each time 
    # the element occurs.
    # n iterations and in each iteration O(1) work: O(n)
    for i in range(len(a)):
        h[a[i]] = i
        
    # n iterations and in each iteration O(1) work: O(n)
    for i in range(len(a)):
        if t - a[i] in h: return (i, h[t - a[i]])
    return (-1,-1)


# ## Exercise
# 
# Test all three programs using ```list(range(10000))``` for the input array and ```20000``` for the number (we know that $2 \cdot 9999 = 19998 < 20000$ so that we exercise the worst case for all three programs).

# In[ ]:




