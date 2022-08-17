# Lecture 4

This lecture is about Dynamic programming.
```{admonition} The Dynamic Programming paradigm
(taken from  [Algorithms Illuminated](http://algorithmsilluminated.org)) 

 1) Identify a relatively small number of subproblems.
 
 2) Show how to quickly and correctly solve *larger* problems given solutions to *smaller* problems.
  
 3) Show how to quickly and correctly infer the final solution from the solutions to all the subproblems. 
 
Almost there: the algorithm you obtain is to systematically solve all the subproblems one by one, working from smallest to largest and extract the final solution from the solutions to the subproblems. 
```
We will guide you trough Python implementations of three examples:

1) Fibonacci numbers.

2) Maximum weight independent sets in path graphs.

3) The Knapsack problem.

In this lecture  we will make clear what the three  steps are in all the examples. 

Dynamic programming lies behind many great algorithms. Check [Algorithms that use Dynamic p
programming](https://en.wikipedia.org/wiki/Dynamic_programming#Algorithms_that_use_dynamic_programming)

As you can see,  it is worth being able to apply  this paradigm for the design of algorithms when you face a problem!



```{tip}
Both Divide & Conquer and Dynamic programming are about finding subproblems. At a first glance it might seem that there are similarities. To understand how they relate to each other we refer you to Section 16.4.4 of the book [Algorithms Illuminated](http://algorithmsilluminated.org).
```






