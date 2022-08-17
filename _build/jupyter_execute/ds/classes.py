#!/usr/bin/env python
# coding: utf-8

# # Classes
# 
# With classes we can define **Abstract Data Types**. You can think of this as extending Python with new types. With classes we say both what the objects (values) of the new type are and also what operations you can do with them.
# 
# The simplest example I can come up with is a data type for *counters*. I have already described it in 
# [A concise presentation of Python](https://veronica-gaspes.github.io/Concise-Python/class-defs.html). The abstract data type is an implementation of something like 
# 
# <img src = "https://i5.walmartimages.com/asr/4cec132e-6c9a-4ea5-88d6-754dcf27c63b_1.a8d67a1b6eeacd6410db8f31ae44aa3a.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff" width = "150">
# 
# In a very abstract fashion this is just a number that can be incremented. If you buy one of those you can press the button and the number is incremented by 1. The guy that checks how many people attend a movie in my local film club uses one of these: he stands at the door and just presses the button when we get into the theatre.
# 
# You can imagine other types of data that are not part of Python. For example bank accounts. For our purposes, a bank account has an owner and a balance (how much money is in the account). The operations are: to deposit and to withdraw money. Here is an implementation. The point of showing you this implementation is for you to distinguish between the instance variables (for the owner and the balance) from the arguments of methods (functions in a class are called methods, and they are used with the . notation as you can see in the exmple directly after the class definition).

# In[1]:


class BankAccount:
    #------
    
    # Construct a bank account for 
    #     - a given person identified by a string with numbers (in Sweden personnummer)
    #     - a start amount of money, by default 0
    # In programs we do not use __init__. Instead we will create a BankAccount as in 
    #  ba_1 = BankAccount('123456')
    # or
    #  ba_2 = BankAccount('123456', 10000)
    
    def __init__(self, identity, amount = 0):
        # instance variables balance and id get their first values
        self.balance = amount
        self.id = identity
       
    # The operation of depositing money
    # updates the value of the instance variable balance.
    # it is used without self, as in 
    #  ba_1.deposit(10000)
    
    def deposit(self, amount):
        self.balance += amount
        
    # The operation of withdrawing  money
    # updates the value of the instance variable balance only when it is possible:
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
       
    
    # A standard operation to that printing or showing a value shows what we want and not just a memory address
    def __str__(self):
        return 'Bank account for ' + self.id + ' with balance ' + str(self.balance)
        
    


# In the following example make sure you understand how ```__init__```, ```__str__```, ```deposit``` and  ```withdraw``` are used and make sure you understand that the values of the instance variables preserve the state of the bank account. 
# 
# What in the definitions of the methods is an argument (```self```) in the uses is the object before the ```.```.
# 
# As you can see, the bank account is the same all along, but the amount of money in the account changes as the program deposits and withdraws.

# In[2]:


ba_1 = BankAccount('123456')
print(ba_1)
ba_1.deposit(10000)
print(ba_1)
ba_1.withdraw(10010)
print(ba_1)
ba_1.withdraw(10)
print(ba_1)


# In[ ]:




