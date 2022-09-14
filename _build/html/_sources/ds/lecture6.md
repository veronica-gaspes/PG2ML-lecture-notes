# Lecture 6
In this chapter we move to data structures that can be used for more general strategies for storing and retrieving. Remember that what we strive for is to as close as possible to $O(1)$ for the operations of insertion and retrieval.

The data structures we explore are *Hash Tables* and *Binary Search Trees*.  

Python provides the abstract data types ```dict``` and ```set``` that are implemented using hash tables. They are incredibly fast for inserting and retrieving.

Binary search trees are not as fast, but on the other hand keep the elements in order, so that on retrieving we can recover the elements in order.

```{Warning}
To my knowledge Python does not use Binary Search Trees in any of its abstract data types. So, what to do if you need one? We present you with a naive implementation, but it has a very bad worst case because we do not keep the tree balanced. You should use some third party implementation of either Red-Black trees or AVL trees ot another implementation that keeps the trees balanced.
```
These data structures address the fact that many times we would like to have collections of data
- that are not indexed by numbers $0 \ldots n$ as in arrays and
- that can grow and shrink during the execution of a program, by adding and removing elements.

> Implementing a phonebook that we can update by adding users, removing users and changing the information associated to a user should not be more difficult than using an array!

In Python there is a data type called ```dict``` that helps with exactly this. We call the indices *keys*.

```Python
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
```
This Python type ```dict``` uses a **hash table** to store the key-value pairs. Hash tables do not support an ordering among the items.

**Binary search trees** provide the same kind of operations but they also maintain an order among the elements in the collection.
