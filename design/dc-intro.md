# Lecture 3

This lecture is about Divide & Conquer.
```{admonition} The Divide & Conquer paradigm
(adapted from  [Algorithms Illuminated](http://algorithmsilluminated.org)) 

 1) *Divide* the input into smaller parts to get subproblems.
 
 2) *Conquer* the subproblems  recursively.
  
 3) *Combine* the solutions to the subproblems into a solution for the original problem.
 
We know what we mean by step 2). 

Steps 1) and 3) are the key! They are very much problem specific. They can be very simple, like divide an array into two halves for 1) or append two arrays for 3). Or they might be more complicated. Of course, the execution time will depend, among other things, on the execution times of these two steps (do check the Master method!)
```
We will guide you trough Python implementations of three examples:

1) Mergesort

2) Finding inversions

3) (We have already discussed this) Karatsuba's algorithm for multiplying integer numbers. In this case we will just discuss how it fits into the Divide & Conquer paradigm.

In this lecture  we will make clear what the three  steps are in all the examples. 

It is interesting that (a variant of)  Mergesort is the algorithm implemented in Python (and Java among other languages) for sorting arrays. It might be the case that if you know something more about the arrays that you are going to sort you would prefer another method (Quicksort) for example. But for sorting arrays for which you know nothing about, Mergesort seems to be the best! 

Also Karatsuba is the algorithm of choice in Python for implementing multiplication of big integers. 

So, it seems that Divide & Conquer can lead to really great algorithms: it is worth mastering this paradigm for algorithm design!



```{warning}
There are chapters of the book that we do not discuss in these lecture notes but that are part of the course. For example, you need to know about the Master method for calculating the asymptotic execution time of algorithms that follow the Divide and Conquer paradigm. The book  [Algorithms Illuminated](http://algorithmsilluminated.org) discusses this in Chapter 4 in Part 1.
```






