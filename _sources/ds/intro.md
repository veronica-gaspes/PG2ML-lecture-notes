# Introduction

Up to this point we have been dealing with algorithms that work on numbers or arrays. At one point we needed sets and we just used Python's implementation. Why did we need a set? Well, for one thing, we did not know how many nodes we would have in the independent set so we could not go for an array. But what is a set in Python?

Data structures are ways of organising data so that **items can be stored and retrieved efficiently**. Depending on what it is that you need to do in the rest of the program that uses the data items you will want to choose among data structures.

Your program might need to retrieve the items depending in the order in which they are inserted. There are two strategies, First In First Out (**FIFO**) and Last In First Out (**LIFO**).

The first strategy corresponds *queues*  and you might be familiar with how it works from your daily queuing! The idea is that in a program you will be able to use variables that are queues, to which you can **add elements (at the back of the queue) and retrieve elements (from the front)**.  The execution time of these operations is **constant**: independent of the number of elements you already have in the queue.

The second strategy corresponds to what in computer science is called a *stack*. Stacks might be a little more unfamiliar! Well, except if you think of stacking up the dishes after washing: you form a pile and when you need dishes to take to the table you take the ones you put last in the pile. So, stacks are piles. The idea is that in a program you will be able to use variables that are stacks, to which you can **add elements (at the back of the stack) and retrieve elements (from the back)**.  The execution time of these operations is constant: independent of the number of elements you already have in the stack.

However, these are not the only strategies for retrieving elements from a collection of items!

 Your program might need to **always retrieve the minimum (or the maximum)** from the collection. It is interesting that even if this is more difficult to achieve, there is a data structure that is very good. It is called a *heap* and it allows you to insert items and retrieve the minimum (or the maximum) very efficiently. These operations are not quite constant time, but they are **logarithmic in the size of the heap (logarithmic in the number of elements in the heap)**. This is great news!

Finally, we will also consider data structures that allow for **more general inserts and lookups** and that are **almost as efficient as arrays** even if the indices can be of (almost) any types and not just numbers from 0 to length! These data structures are *Hash Tables* and *Binary Search Trees*.

Heaps, Hash Tables and Binary Search Trees are already implemented in Python:
* dictionaries and sets use hash tables,
* there are operations for building up heaps in lists,
* and, there are ordered dictionaries and sets that use binary search trees.

These three data structures we will discuss are already implemented in Python (and in most programming languages).

We will look at what operations they support and we will look at the running time behaviour of the operations.

We start however by looking at lists in Python in order to understand why we need better data structures!

When we discuss implementations of data structures we will introduce how to define and use *classes* in Python.
