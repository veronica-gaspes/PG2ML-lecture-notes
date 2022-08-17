#!/usr/bin/env python
# coding: utf-8

# # Understanding ```for``` loops
# 
# How does a ```for``` loop work? What happens when we use a ```for``` loop (or two!)?
# 
# Without solving a specific problem, the following examples are designed to illustrate the execution of ```for``` loops.  
# 
# We start with one loop repeating one command: print the value of the control variable. This allows us to see how many times the command inside the ```for``` loop is repeated and what values the control variable takes in each iteration.

# In[1]:


size = 10

for i in range(size):
    print('i:', i)


# Once the for loop is done the program can continue. 
# 
# To illustrate this we add a command inside the loop to increment a counter in every iteration. After the loop terminates the value of the counter is the number of times the command inside the loop was executed. We add a command to print this value.
# 
# Observe that *printing the value of the control variable* is done on every turn of the loop while *printing the value of the counter* is only done once: after the loop has done all its iterations.

# In[2]:


size = 10
count = 0

for i in range(size):
    count += 1
    print('i:', i)
    
print('nr of iterations:', count)


# Of course, what the program does after the loop terminates could be any command. 
# 
# We add another loop with its own control variable and its own counter. Observe that we add some white spaces in the print statement in the second loop to make it easier to follow the output.

# In[3]:


size = 10
count_i = 0
count_j = 0

for i in range(size):
    print('i:', i)
    count_i += 1
    
for j in range(size):
    print('   j:',j)
    count_j += 1
    
print('count on i:', count_i)
print('count on j:', count_j)


# The command inside the for loop can also be any command, for example another loop.
# 
# We modify the program to place the second loop as part of the command that the first loop repeats each iteration.  Because the output becomes too long we also changed the value of ```size``` to 5.
# 

# In[4]:


size = 5
count_i = 0
count_j = 0

for i in range(size):
    print('i:', i)
    count_i += 1
    for j in range(size):
        print('   j:', j)
        count_j += 1
        
print('count on i:', count_i)
print('count on j:', count_j)


# Given that the output becomes too long to observe for bigger values of ```size```, we remove the prints but keep the counts. 
# 
# First check the example with the second loop after the first loop:

# In[5]:


size = 10
count_i = 0
count_j = 0

for i in range(size):
    #print('i:', i)
    count_i += 1
    
for j in range(size):
    #print('   j:',j)
    count_j += 1
    
print('count on i:', count_i)
print('count on j:', count_j)


# And now the example with the second loop as part of the command that the first loop repeats (this is usually called nested loops):

# In[6]:


size = 5
count_i = 0
count_j = 0

for i in range(size):
    #print('i:', i)
    count_i += 1
    for j in range(size):
        #print('   j:', j)
        count_j += 1
        
print('count on i:', count_i)
print('count on j:', count_j)


# Now we can try the example with nested loops for size 10. Do it: change the value of the variable ```size``` to 10 and re-run the cell. You should get the output:
# 
# ```
# count on i: 10
# count on j: 100
# ```
# 

# Now you should experiment increasing the value of ```size``` in both examples (consecutive loops and nested loops). Try 10, 100, 1000, 10000. 
# 
# Do you experience the difference in execution time? 
# 
# Notice that you multiply the value of ```size``` by 10 for each of the experiments.
# 
# The execution time increases as ```size``` increases. 
# 
# But **at what rate**  execution time increases is different for consecutive loops than  for nested loops. This is related to the fact that the number of times that the command in the second loop is executed is very different in the two scenarios!
