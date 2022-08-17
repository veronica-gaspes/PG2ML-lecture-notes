#!/usr/bin/env python
# coding: utf-8

# # Queues
# 
# Some programs need to retrieve data in the same order as it was stored. We call this to *enqueue* items of data. We could imagine doing this by using a list to add elements at the end and retrieve them from the front, as in the following example:

# In[1]:


q = []

for i in range(10):
    # enqueue by placing at the end:
    q = q + [i]
print(q)
print()

for i in range(10):
    # dequeue by removing from the front:
    print('Service first in queue:', q.pop(0))
    print(q)
    print()


# The problem is that we know that these operations are linear time! We would like to have constant time instead (not more expensive than updating / reading an array). 
# 
# This can be achieved by keeping track of the first and the last element and keeping the elements together via links. We call the pair of an element and a link a Node. We use a class with the name ```_Node``` for these nodes (remember that we use the convention of using an underscore at the begining of a name to indicate that it is an auxiliary function or name). As you can see in the definintion in next cell, a node has two instance variables: an element (item) and a link (next).
# 
# The class for queues is called ```Queue``` (no underscore!) and has two instance variables: the first node and the last node! It has methods to add items (```enqueue```)and to remove items (```dequeue```). Also for testing emptiness, for the number of elements and to make a string of the content.
# 
# You to inspect the code! Confirm that all operations are constant time (except ```__str__```!)

# In[2]:


# From the book Introduction to Programming in Python, chapter 4.3 on Stacks and Queues:
# https://introcs.cs.princeton.edu/python/43stack/

#----------------------------------------------------------------------

# A _Node object references an item and a next _Node object.
# A Queue object is composed of _Node objects.

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item
        self.next = next  # Reference to the next _Node object



class Queue:

    #-------------------------------------------------------------------

    # Construct the Queue object self as an empty Queue object.

    def __init__(self):
        self._first = None  # Reference to first _Node
        self._last = None   # Reference to last _Node
        self._length = 0    # Number of items

    #-------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def is_empty(self):
        return self._first is None

    #-------------------------------------------------------------------

    # Add item to the end of self.

    def enqueue(self, item):
        oldLast = self._last
        self._last = _Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._length += 1

    #-------------------------------------------------------------------

    # Remove the first item of self and return it.

    def dequeue(self):
        item = self._first.item
        self._first = self._first.next
        if self.is_empty():
            self._last = None
        self._length -= 1
        return item

    #-------------------------------------------------------------------

    # Return the number of items in self.

    def __len__(self):
        return self._length

    #-------------------------------------------------------------------

    # Return a string representation of self.

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s


# Here is the same example as before but using this implementation for queues:

# In[3]:


q = Queue()

for i in range(10):
    q.enqueue(i)
    
print(q)
print()

for i in range(10):
    # dequeue by removing from the front:
    print('Service first in queue:', q.dequeue())
    print(q)
    print()


# In[4]:


# In case we do not know how many times we can dequeue we can test for emptyness:

q = Queue()

for i in range(10):
    q.enqueue(i)
    
print(q)
print()

while not q.is_empty():
    # dequeue by removing from the front:
    print('Service first in queue:', q.dequeue())
    print(q)
    print()


# ## Listing the contents of a folder
# 
# And now an example. Say you want to list the contents of a folder and of all folders under this one. In Python you can get a list of names of files and folders (directories) using the method ```listdir``` in the module ```os```.
# 
# Here is how my directory for this lecture notes looks like:

# In[5]:


import os


# In[6]:


for name in os.listdir('..'):
    print(name)


# Not all of these are directories, so if we want to list the contents of the directories we need to test whether a name corresponds to a directory. This can be done in Python using the method ```is_dir``` in the module ```os.path```. 
# 
# So, here we list all sub-directories also:

# In[7]:


import os
for name in os.listdir('..'):
    print(name)
    if os.path.isdir('../' + name):
        print(os.listdir('../' + name))
        


# We would like to list as long as there are files, as deep as needed. We do it level by level, using a queue! This algorithm is called Breadth First Search. 
# 

# In[8]:


def list_dir_tree(path):
    q = Queue()
    q.enqueue(path)
    
    while not q.is_empty():
        path = q.dequeue()
        print(path)
        if os.path.isdir(path):
            for name in os.listdir(path):
                q.enqueue(path + '/' + name)
     
    


# In[9]:


list_dir_tree('..')


# Make sure you understand the algorithm and the output!  Can you find the source of this notebook? It is 
# 
# ```../ds/queues.ipynb```.
# 
# 
# The first thing is the starting path, then file and directory names directly under it, then next level for those names that were directories, etc. 
# 
# I would recommend you to try to follow the algorithm by hand with a directory structure such as
# ```text
# A
#     B
#         e
#         f
#         
#     c
#     
#     D
#         g
#         H
#             i 
#             j
# ```
# where capital letters are dictionaries and small letters are files. Make sure you keep track of the queue! You should produce the output:
# 
# ```text
# A
# 
# A/B
# A/c
# A/D
# 
# A/B/e
# A/B/f
# A/D/g
# A/D/H
# 
# A/D/H/i
# A/D/H/j
# ```
# where I have added new lines to mark the depth levels.

# By the way, what would the algorithm do if we used a stack instead?

# In[10]:


def list_dir_tree_stack(path):
    s = []
    s.append(path)
    
    while not s == []:
        path = s.pop()
        print(path)
        if os.path.isdir(path):
            for name in os.listdir(path):
                s.append(path + '/' + name)


# In[11]:


list_dir_tree_stack('..')


# As you can see it goes as deep as possible (instead of level by level) this algorithm is called DFS: Depth First Search.
# 
# Make sure you can follow the stack in the example with letters we suggested before. Here is the output you should expect:
# 
# ```text
# A
# A/B
# A/B/e
# A/B/f
# A/c
# A/D
# A/D/g
# A/D/H
# A/D/H/i
# A/D/H/j
# ```
