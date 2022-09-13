# Heaps

We continue with our main theme: we need to store and retrieve items of data as the program runs.

But now, we would like to be able to retrieve always the least element among the items in the collection. And we would like to be able to store and retrieve in *almost* constant time (because these operations will often be done as part of an iteration).

We cannot think of using a list because, in order to retrieve the minimum element in constant time we would need to keep the list sorted. And to do so, we would need to insert the new element in its place in the order, and this takes linear time to do.

This is the problem that heaps solve!

A **heap**  provides the operations **insert** and **extract min**:

- **insert** adds an element to an existing heap.

- **extract min** removes and returns the item with the smallest *key* from an existing heap.

We will consider that the items we insert and extract from a heap are so called *key-value pairs*. This is because we often use the *key* to order the items, not the items themselves. You can think of the *key* for example as a priority. The items could be anything, even things for which we do not want to define an order!

Heaps provide these two operations in *almost constant* time. In fact, the time it takes to insert or extract the smallest element from a heap depends on how many elements there  are in the heap already. But both operations are $O($log$ \,n)$ (where $n$ is the number of elements already in the heap).

The implementation in Python provides also operations to make a heap from a list in linear time: $O(n)$ and to peek the smallest element in the list without retrieving it in constant time $O(1)$.
