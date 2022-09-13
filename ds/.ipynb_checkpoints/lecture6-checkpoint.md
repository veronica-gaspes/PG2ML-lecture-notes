# Lecture 6
In this chapter we move to data structures that can be used for more general strategies for storing and retrieving. Remember that what we strive for is to as close as possible to $O(1)$ for the operations of insertion and retrieval.

The data structures we explore are *Hash Tables* and *Binary Search Trees*.  

Python provides the abstract data types ```dict``` and ```set``` that are implemented using hash tables. They are incredibly fast for inserting and retrieving.

Binary search trees are not as fast, but on the other hand keep the elements in order, so that on retrieving we can recover the elements in order. 

```{Warning}
To my knowledge Python does not use Binary Search Trees in any of its abstract data types. So, what to do if you need one? We present you with a naive implementation, but it has a very bad worst case because we do not keep the tree balanced. You should use some third party implementation of either Red-Black trees or another implementation that keeps the trees balanced.
```

