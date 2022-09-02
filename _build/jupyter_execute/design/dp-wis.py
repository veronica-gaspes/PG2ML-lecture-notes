#!/usr/bin/env python
# coding: utf-8

# # Maximum independent set for weighted path graphs
# 
# 
# ## Definitions and examples
# 
# A path graph looks like a line of dots connected by line segments. The dots are called vertices or nodes. The line segments are called edges. Here is an example:
# 
# $$\bigcirc \rule[2pt]{1cm}{0.4pt} \bigcirc \rule[2pt]{1cm}{0.4pt} \bigcirc \rule[2pt]{1cm}{0.4pt} \bigcirc \rule[2pt]{1cm}{0.4pt}  \bigcirc \rule[2pt]{1cm}{0.4pt} \bigcirc $$
# 
# When we associate a weight or cost with the nodes we cal it a weighted path graph. We can then use an array to describe a path graph: the indices are the *names* of the nodes and the content is the weight of the index node.
# 
# A path graph with as above would have nodes 0, 1, 2, 3, 4 and 5. A weighted variant can be given by the array
# 
# ```Python
# [6,10,1,1,1,2]
# ```
# to mean that node 0 has weight 6, node 1 has weight 10, nodes 2, 3 and 4 have weight 1 and node 5 has weight 2.
# 
# Now that we understand what a weighted path graph is, lets look at *independent sets*. 
# 
# An independent set is a set of nodes that do not share an edge. Here are **some** independent sets for the path graph we are using:
# 
# $$ \emptyset,  \{0\},  \{1\}, \{2\}, \{3\}, \{4\}, \{5\}, \{0,2\}, \{0,3\}, \{1,3,5\}$$
# 
# There are of course more that you might try to find. 
# 
# The following is **not** an independent set: $ \{0,2,3\} $. This is because 2 and 3 are endpoints of the same edge.  
# Given an independent set in a weighted path graph, we can calculate the total weight of the set by adding the weights of the nodes in the set. In our example
# 
# - the independent set $ \emptyset $ has weight 0
# 
# - the independent set $ \{0\} $ has weight 6
# 
# - the independent set $\{1,3,5\}$ has weight 13
# 
# ## Problem statement
# 
# Given a weighted path graph find an independent set of maximum weight. All weights are $ > 0$.
# 
# ## Finding an algorithm
# 
# The book  [Algorithms Illuminated](http://algorithmsilluminated.org) discusses this problem in detail in Chapter 16 in Part 3. Among other things it discusses two approaches, both of which fail to design a correct algorithm. Finally it makes an attempt using Dynamic programming and that is what we will follow here.
# 
# Here is the sketch of the paradigm once more:
# 
# 1. Identify a relatively small number of subproblems.
# 
# 2. Show how to quickly and correctly solve *larger* problems given solutions to *smaller* problems.
# 
# 3. Show how to quickly and correctly infer the final solution from the solutions to all the subproblems. 
# 
# > The algorithm you obtain is to systematically solve all the subproblems one by one, working from smallest to largest and extract the final solution from the solutions to the subproblems. 
# 
# ### How can we identify *the small number of subproblems?*
# 
# We can start by assuming that we have a solution for a given size and try to see what components, in terms of solutions to smaller problems it can have. **Notice that we do not look at the input size but at how the solution might look like!*
# 
# Consider the example, and say that we have a solution for the whole path graph: we have an independent set $S$ of maximum weight for the whole path graph. 
# 
# We do not know much about this set $S$! 
# 
# But, given that we cannot have the two last nodes in the set and that the weights are positive, the set will either include the last node (node 5) or it will not. If not, it will include the next to last (node 4)! If it does,  it will not include the next to last! So, lets consider these two cases:
# 
# * node 5 belongs to $S$. But in this case node 4 cannot belong to $S$ so in some way there has to be a solution for the graph with nodes up to node 3 (remove 2 nodes from the path graph) that can be used to form our solution. We take this solution and add node 5 with its weight. 
# 
# * node 5 does not belong to $S$. Then, the solution is the same as the solution for the smaller graph upto node 4!
# 
# So, we pick two smaller subproblems: the path graph without the last node (P1) and the path graph without the two last nodes (P2)
# 
# How can we use these two to form a solution for the whole path graph? Well, it depends on the weight of the last node. Say that the solution for P1 has total weight W1 and the solution for P2 has total weight W2. 
# 
# * If W2 + weight of final node  $>$ W1 we use the solution for P2 and add the last node with its weight.
# 
# * If not, we use the solution for P1 (we do not use the last node in the solution).
# 
# If we do this from the smallest path graphs that form the path graph in our problem until we have all the nodes in the graph, we just need to take the solution for the longets path graph!
# 
# Let's look at the example, starting with the smallest path graph and building the solutions for the longer and longer path graphs using these ideas:
# 
# 1. The solution for the path graph with only node 0 is the independent set ${0}$ with weight 6.
# 
# 2. The solution for the path graph with nodes 0 and 1 can only have one node (it has to be an independent set!). So, it will pick node 0 or node 1, the one with highest weight. In our case the solution is ${1}$ with weight 10.
# 
# 3. The solution for the path graph with nodes 0, 1 and 2 is found by picking the best between:
# 
#    a. The solution for the path graph 0, 1: weight 10
#    
#    b. The solution for the path graph 0 and the node 2: weight 6 + 1
#         
#    We keep the same solution as for 0, 1 with weight 10.
#    
# 4. The solution for the path with nodes 0, 1, 2, 3 is found by picking the best between:
# 
#    a.  The solution for path graph 0, 1, 2: weight 10
#     
#    b.  The solution for path graph 0, 1 and node 3: weight 10 + 1
#     
#    We take the solution for path graph 0, 1 and add node 3: weight 10 + 1
#    
# 5. The solution for the path with nodes 0, 1, 2, 3, 4 is found by picking the best between:
# 
#    a.  The solution for path graph 0, 1, 2, 3: weight 11
#         
#    b.  The solution for path graph 0, 1, 2 and node 4: weight 10 + 1
#     
#    They are the same! We could pick any of them. Both have weight 11.
#    
# 6. The solution for the path with nodes 0, 1, 2, 3, 4, 5 is found by picking the best between:
# 
#    a.  The solution for path graph 0, 1, 2, 3, 4: weight 11
#         
#    b.   The solution for path graph 0, 1, 2, 3 and node 5: weight 11 + 2
#     
#    We take the solution for path graph 0, 1, 2, 3 and add node 5: weight 11 + 2.
#    
# The solution to the problem has weight 13 and we can reconstruct it from the back: it uses node 5 (and then it does not use node 4) so we go to the solution for node 3: it uses node 3 (and then it does not use node 2) so we go to the solution for node 1: it uses node 1 (and then it does not use node 0). So: the independent set of with weight 13 is $\{1, 3, 5\}$
# 
# Again, as in Fibonacci, we see the need for an array that we start filling in using the weights of the nodes in the path graph.

# In[1]:


# wpg is a weighted path graph given as an array: the indices are the nodes and the elements are the weights.

def dp_wis(wpg):
    
    n = len(wpg)
    solution_weights = [0] * n
    
    # For a path graph with only one node the solution uses that node!
    solution_weights[0] = wpg[0]
    
    # For a path graph with two nodes, only one can be in the independent set: the one with highest weight
    if wpg[0] > wpg[1]:
        solution_weights[1] = wpg[0]
    else:
        solution_weights[1] = wpg[1]
      
    # In all other cases pick the best between the solution for the path graph with one less node
    # or the solution fot the path graph with 2 less nodes and add the last node.
    for i in range(2, n):
        solution_weights[i] = max(solution_weights[i - 1], 
                                  solution_weights[i - 2] + wpg[i])
    
    # Finally, the solution is the last element!
    return solution_weights[n-1]
        


# In[2]:


dp_wis([6,10,1,1,1,2])


# In[3]:


# the example in the book:
dp_wis([1,4,5,4])


# Now we want to add the *reconstruction*: we not only want the weight of the solution, we also want the independent set! 
# 
# In the book the algorithm uses a *set* $S$ to collect the nodes of the independent set. We do the same in Python even if we have not yet discussed sets. We will touch on sets in the lecture notes for data structures! For the moment we just use it. Here is what you have to know:
# 
# * You can create the empty set using ```set()```
# 
# * You can add elements ```e``` to a set ```s``` by doing ```s.add(e)```
# 
# So, here is the algorithm that calculates the weight of the independent set with maximum weight in a weighted path graph **and** forms the independent set with that weight (and you see why we cannot get rid of the array as we did in Fibonacci!):

# In[4]:


# And now with the re-construction steps:

def dp_wis_with_reconstruction(wpg):
    
    n = len(wpg)
    solution_weights = [0] * n
    
    # For a path graph with only one node the solution uses that node!
    solution_weights[0] = wpg[0]
    
    # For a path graph with two nodes, only one can be in the independent set: the one with highest weight
    if wpg[0] > wpg[1]:
        solution_weights[1] = wpg[0]
    else:
        solution_weights[1] = wpg[1]
      
    # In all other cases pick the best between the solution for the path graph with one less node
    # or the solution fot the path graph with 2 less nodes and add the last node.
    for i in range(2, n):
        solution_weights[i] = max(solution_weights[i - 1], 
                                  solution_weights[i - 2] + wpg[i])

    # Finally, the solution is the last element!
    
    # Reconstruction ()
    wis = set()
    i = n - 1
    while i >= 1:
        if solution_weights[i-1] > solution_weights[i-2] + wpg[i]:
            i = i - 1
        else:
            wis.add(i)
            i = i - 2
            
    if i == 0: wis.add(0)
        
    # the set and the weight
    return (wis, solution_weights[n-1])


# In[5]:


dp_wis_with_reconstruction([6,10,1,1,1,2])


# In[6]:


# the example in the book:
dp_wis_with_reconstruction([1,4,5,4])

