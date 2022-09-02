#!/usr/bin/env python
# coding: utf-8

# # The knapsack problem
# 
# Imagine wanting to take with you very valuable things as you move to another country. Maybe taking all of them is not possible: they weigh too much for what your flight allows for. How do you choose what to take with you and what to leave behind?
# 
# How much weight you are allowed for your luggage is given, the airline has decided. 
# 
# The weights of the items are as they are. 
# 
# Imagine assigning a value to each of the items reflecting how important each item is for you. 
# 
# We hope to calculate what items to put in the luggage so that you get as much value as possible while keeping the total weight below the limit imposed by the airline.
# 
# In computer science this is one of many possible formulations of the Knapsack problem (the knapsack being your luggage). You will find other formulations in the Wikipedia entry [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem#Applications). The book [Algorithms Illuminated](http://www.algorithmsilluminated.org) puts it as 
# 
# > Whenever you have a scarce resource that you want to use in the smartest way possible, you are talking about the knapsack problem. On which goods and services should you spend your paycheck to get the most value? Given an operating budget and a set of job candidates with different productivities and requested salaries, whom should you hire? These are examples of knapsack problems.
# 
# ## Definitions and examples
# 
# In an instance of the Knapsack problem we get some items for which we know their value and their size, and we also get a so called capacity. 
# 
# The result will be a list of items for which the total value is as big as possible and the total size is at most the capacity. 
# 
# We do not need to say what the values or the sizes or the capacity stand for, it might be different things for different applications.
# 
# Here is an example:  
# ### Capacity:
# ```10```
# ### Items:
# ```0,1,2,3,4```
# ### Values:
# ```5,4,3,2,1```
# ### Sizes:
# ```2,4,1,5,3```
# 
# 
# Or with a table
# 
# | Item | Value | Size |
# |:----:|:-----:|:----:|
# |0|5|2|
# |1|4|4|
# |2|3|1|
# |3|2|5|
# |4|1|3|
# 
# A list with all the items is not a result: the total size is ```15``` while the capacity is only ```10```.
# 
# Can we achieve a total size of exactly ```10``` with some of the items? Well yes! Take all of the items except the one with size ```5``` (item ```3```): ```[0,1,2,4]```. But also these lists have weight ```10```: ```[0,3,4]``` and ```[1,2,3]```. 
# 
# What are the values of these lists of items?
# 
# ```[0,1,2,4]``` has value ```5+4+3+1 = 13```
# 
# ```[0,3,4]``` has value ```5+2+1 = 8```
# 
# ```[1,2,3]``` has value ```4+3+2 = 9```
# 
# So, among these we would pick the list of objects ```[0,1,2,4]``` that has the highest value!
# 
# But now the question is, could we have a higher value even if the size is not exactly ```10```?
# 
# The highest value we can achieve (all items) is ```15```. We already know that we cannot hope for that because it uses all items and the total size is more than ```10```! What about ```14```? The only way that can be is by not using element ```4``` (value ```1```): ```[0,1,2,3]```. But then the size is ```2+4+1+5 = 12``` which is more than ```10```!
# 
# So it seems we have a result: the list ```[0,1,2,4]``` with value ```13``` and size ```10```.
# 
# Now we will go for designing an algorithm that can solve any instance of the problem. We will follow the ideas of Dynamic Programming to design the algorithm. This is explained in detail in chapter 16.5 in part 3 of the book [Algorithms Illuminated](http://www.algorithmsilluminated.org).
# 
# ## Problem statement
# 
# The input to the problem are 1) the list of values, 2) the list of sizes and 3) the capacity. The output is a subset of the items such that its total size is at most the capacity and its total value is as large as possible. 
# 
# ## Finding the algorithm
# 
# The book  [Algorithms Illuminated](http://algorithmsilluminated.org) discusses this problem in detail in Chapter 16.5 in Part 3.
# 
# Recall the three steps:
# 
# 1. Identify a relatively small number of subproblems.
# 
# 2. Show how to quickly and correctly solve *larger* problems given solutions to *smaller* problems.
# 
# 3. Show how to quickly and correctly infer the final solution from the solutions to all the subproblems.
# 
# > The algorithm you obtain is to systematically solve all the subproblems one by one, working from smallest to largest and extract the final solution from the solutions to the subproblems. 
# 
# For step 1 we do as usual, we carefully inspect a solution to a problem to see whather we can use some information about how that solution should *look like*. **Again, in contrast to Divide and Conquer, we do not start by looking at the size of the input to find subproblems, instead we look at a solution to see how it is composed of solutions to smaller problems.**
# 
# Say that you have a solution for an instance of the knapsack problem given by values $v_0, \ldots, v_{n-1}$, sizes $s_0, \ldots, s_{n-1}$ and capacity $C$. A soultion will be a subset of the items $S \subseteq \{0,\ldots, n-1\}$ with maximal value and total size at most $C$. 
# 
# Again, we inspect it by looking at the items that might be included in $S$ and we consider whether $S$ uses one of the items or not. In order to make our task easy, we consider the last item, the one called $n-1$. There are only two cases to consider: either $n-1 \in S$ or $n-1 \notin S$!
# 
# ### Quiz
# Go back to the example and check what is the case for the solution we suggested. Check, what is $n$? Does the solution use item $n-1$?
# 
# Let's consider the two cases to see what we can observe.
# 
# * If the last item is not part of $S$ we could also consider it as a solution to the knapsack problem instance with the same capacity but with one less element: the size is at most the capacity and there could not be an item that improved the total value (we would have used it in $S$ already!). So we can say that if the last element is not used in $S$ then $S$ is in itself a solution to a smaller instance of the knapsack problem with values $v_0, \ldots, v_{n-2}$,  sizes $s_0, \ldots, s_{n-2}$ and capacity $C$.
# 
# * If the last item is part of $S$ it is there contributing its value and its size! How can this come from a solution to another instance of the knapsack problem? It cannot be a solution to an instance with less items but has the same cpacity, because a solution to that problem might not leave place for the size of the last item! But this suggests another instance: less items and a capacity that leaves place for the size of the last item: $C - s_{n-1}$!
# 
# And this gives us a *nice(?)* recursion for the maximum total value of a subset of the items with total size smaller than the capacity
# 
# $$ V_{i,C} = \text{max}\{V_{i-1,C}, V_{i-1, C-s_i} + v_i\} $$
# 
# This is not that nice! There are many re-calculations. But we can try to find a way to build up the results starting from solutions to small problems and building solutions to larger problems. It is more difficult than before because we not only go back removing items, we also reduce the capacity in one of the cases!
# 
# What we need to build is solutions for items and capacities: we need a 2-d array! The solution will be found when we look at the array in the position that stands for the instance with all items and the original capacity!
# 
# Finally, here is the program in Python for the algorithm presented in the book. 
# 
# The array ```A``` has two dimensions. One of the dimensions is what items are used (0 items, 1 item, two items, etc) and the other dimension is for all capacities between 0 and the capacity that is an input to the problem.

# In[1]:


# The Dynamic Programming solution to the knapsack problem
# For 
# items             0,  1,  2,  etc 
# that have values  v0, v1, v2, etc 
# and sizes         s0, s1, s2, etc
# find the items with maximum total value 
# such that the total size is not larger than a given capacity C
# sizes and the capacity are non negative integer values.

def dp_knapsack(vals, sizes, C):
    n = len(vals)
    A = [None] * (n+1)
    for x in range(n+1):
        A[x] = [0] * (C+1)
        
    # A[0][c] has already 0s (using 0 items, for all capacities, the value is 0!)
    for i in range(1, n+1):
        for c in range(C+1):
            if sizes[i-1] > c: # sizes are numbered from 0!
                A[i][c] = A[i-1][c] # there is no other choice!
            else: 
                A[i][c] = max(A[i-1][c], 
                              A[i-1][c - sizes[i-1]] + vals[i-1])
    return A[n][C]


# ## Quiz
# What are the dimensions of the array ```A``` for the example we used (5 items, capacity 10). 
# 
# 
# ## Exercise
# Build the array for the example and identify the solution in the array.
# 
# ## Exercise
# Use the program for the example. How can you try it using the items in different orders?
# 
# ## Quiz
# The array contains only values. Can you say what items are in the solution?
# 
# 
# ## Quiz
# What is the asymtotic execution time of the algorithm? 
# 
# ## Exercise
# Write a program for the recursive version and do experiments to compare how the  execution time of both programs grows with the size of the problem. 
# 
# 

# In[ ]:




