#!/usr/bin/env python
# coding: utf-8

# # Heaps
# 
# We continue with our main theme: we need to store and retrieve items of data as the program runs.
# 
# But now, we would like to be able to retrieve always the least element among the items in the collection (the smallest element, the minimum). And we would like to be able to store and retrieve in *almost* constant time (because these operations will often be done as part of an iteration, we hope for iterations that are linear).
# 
# We cannot think of using a list because, in order to retrieve the minimum element in constant time we would need to keep the list sorted. And to do so, we would need to insert the new element in its place in the order, and this takes linear time to do.
# 
# This is the problem that heaps solve!
# 
# A **heap**  provides the operations **insert** and **extract min**:
# 
# - **insert** adds an element to an existing heap.
# 
# - **extract min** removes and returns the item with the smallest *key* from an existing heap.
# 
# In most applications of heaps, the items we insert and extract from a heap are so called *key-value pairs*. This is because we often use the *key* and not the values themselves to order the items. You can think of the *key* for example as a priority. The items could be anything, even things for which we do not want to define an order!
# 
# Heaps provide these two operations in *almost constant* time. In fact, the time it takes to insert or extract the smallest element from a heap depends on how many elements there  are in the heap already. But both operations are $O($log$ \,n)$ (where $n$ is the number of elements already in the heap).
# 
# The implementation in Python provides also operations to make a heap from a list in linear time ($O(n)$) and to peek the smallest element in the list without retrieving it in constant time ($O(1)$).
# 
# 
# # Heaps in Python
# Python uses lists to implement heaps. In order to use a list as a heap you need to use operations in the module *heapq* (that you need to import). 

# In[1]:


import heapq


# ## Creating a heap from elements in a list
# Sometimes you already know what elements (at least to start with) you want in your heap. In this case you need to transform your list in a heap. The function is 
# ```Python
# heapq.heapify(x)
# ```
# > Transform list ```x``` into a heap, in-place, in linear time.
# 
# Remember that operations that work on a collection and are linear are very good! 
# 
# We illustrate the use of ```heapify``` starting from a list with 1000 elements in random order.
# 
# We print the first 20 elements of the elements in the list and then we print the first elements of the heap (that is a list but with the elements organised in a very special way) so that you can see that the list has been modified.
# 
# 

# In[2]:


import random


# In[3]:


elems = list(range(9999))
random.shuffle(elems)
print(elems[0:20])
heapq.heapify(elems)
print(elems[0:20])


# You can run the code several times. You will observe that no matter the order of the shuffled list, the elements in the heapified list are somewhat ordered (the small elements are at the begining, though not completely ordered).  
# 
# The heapified list keeps the values organised in such a way that the element in position ```k``` is smaller or equal than the elements in positions ```2*k+1``` and ```2*k+2```. 
# 
# Can you see this?
# 
# What are the elements in positions 0, 1, 2? And in positions 1, 3, 4? and in positions 2, 5, 6? 
# 
# Instead of printing the first 20 values you can check whether the list os heap organized using the function:
# 
# ```Python
# def heap_organised(lst):
#     return all([lst[k] <= lst[2*k+1] 
#                   and 
#                 lst[k] <= lst[2*k+2]
#                 for k in range(len(elems)//2-2)
#                ]
#             )
# ```
# 
# Make sure you understand the code. If you don't: ask your teacher! 
# 
# Use it as follows:
# ```Python
# elems = list(range(9999))
# random.shuffle(elems)
# heap_organised(elems)
# heapq.heapify(elems)
# heap_organised(elems)
# ```
# 
# 
# 
# 
# ## Adding elements to a heap
# 
# Either if you start from the empty heap (actually the empty list ```[]```) or from a list that you heapified, it is always possible to insert more elements. This has to be done with the heap operation for inserting so that the heap organisation in the list is preserved. 
# 
# Here is an example starting from the empty list, and inserting elements in the reversed order. We print the list of elements inserted and the heap so that you see the consequences of using the heap insertion function: the elements are kept *heap organized*!

# In[4]:


# We use variable h for the heap.

h = [] 
lst = list(reversed(range(20)))
print(lst)
for i in lst:
    heapq.heappush(h,i)
    print(h)


# ### Quiz
# 
# In a heap (in Python a list that is heap organised), what can you say about the element in position 0 of the list?

# If you have a heap (in Python this means a list that is heap organised), then using the function 
# 
# ```heappush(heap, item)``` 
# 
# to add an item to the heap results in a list that includes the new item and is heap organised. 
# 
# If you tried to keep the list sorted it would take linear time $O(n)$. Keeping the list heap organised takes only $O($log$ \,n)$
# 
# ## Retrieving the minimum element from the heap
# In order to retrieve the least element in the heap you need to use the operation 
# 
# ```Python
# heapq.heappop(heap)
# ```
# > Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. **To access the smallest item without popping it, use heap[0]**.
# 
# In the quote *maintaining the heap invariant* means keeping the list heap organised. Here is an example.

# In[5]:


size = 20
lst = list(reversed(range(size)))
print('lst :', lst)
print()
heapq.heapify(lst)
print('heapified lst: ', lst)
print()
for i in range(size):
    print('min: ', heapq.heappop(lst))
    print('lst: ', lst)
    print()


# ## Some applications of heaps
# 
# One very immediate application of heaps is to sort a list (or an array) in $O(n $log$ \, n)$. The algorithm is called *heap sort*. 

# In[6]:


def heapsort(a):
    h = []
    for x in a:
        heapq.heappush(h,x)
    # at this point:
        # a is intact 
        # and all the elements are heap organised in h
        
    # we now overwrite a with the elements in order!    
    for i in range(len(a)):
        a[i] = heapq.heappop(h)
        


# ### Theory exercise
# Explain why the running time is $O(n $log$ \, n)$.
# 
# ### Comment:
# Heap sort uses the same idea as *selection sort*: find the smallest elememnt and put it in the first position, then find the next smallest element and put it in the second position, and so on. However, selection sort is $O(n^2)$ and thus infeasible!
# 
# > Choosing a suitable data structure can turn an algorithm from infeasible to feasible!
# 
# ### Programming exercise
# Write a function ```heapsorted``` that instead of modifying the input array returns a sorted version of the array, keeping the input array as it was. 
# 
# Yet another application of heaps is to calculate order statistics: pick the $k$-th smallest element in an array. 
# 
# ### Programming exercise 
# (from [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/) by R. Sedgewick and K. Wayne)
# 
# 
# Design a $k $log$ \,k$ algorithm to find the $k$-th smallest item in a min-oriented binary heap $H$ containing $n$ items.
# 
# *Solution*. Build a new min-oriented heap $H'$. Do not modify $H$. Insert the root of $H$ into $H'$ along with its heap index 0. Now, repeatedly delete the minimum item $x$ in $H'$ and insert into $H'$ the two children of $x$ from $H$. The $k$-th item deleted from $H'$ is the $k$-th smallest item in $H$.
# 
# Note: you need to insert pairs to the heap $H'$: the first component of a pair is the element in the heap $H$ and the second component is the index in the organised list!
# 
# Write a program that uses this method to find the $k$-th smallest element in an array.
# 
# ### Theory exercise
# What is the Big-$O$ execution time of the algorithm? And of the program (or the algorithm, but starting from the array).
# 
# 

# In[7]:


# Solution to programming exercise
import heapq
def k_smallest(a, k):
    
    # h is a heapified!
    heapq.heapify(a)
    
    h_prime = [(a[0],0)]
    
    for i in range(1, k):
        (v, ix) = heapq.heappop(h_prime)
        if 2*ix + 1 < len(a): heapq.heappush(h_prime, (a[2*ix+1], 2*ix+1))
        if 2*ix + 2 < len(a): heapq.heappush(h_prime, (a[2*ix+2], 2*ix+2))
    (v, _) = heapq.heappop(h_prime)
    return v
        


# In[8]:


import random
lst = list(range(100000))
random.shuffle(lst)
k_smallest(lst,2)


# In[ ]:




