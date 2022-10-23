# Hashmaps
 
## What is a hash function?
A hash function is a function that convert data from an arbitrary size to a fixed size (usually 32-bit integer)
Arbitrary Value -> hash_function() -> 32-bit integer (hash value)
A valid hash function must always return the same hash value for identical inputs. If two different values hash to the
same value that is what we call a collision
Good hash functions have those attributes:
    - Easy to calculate hash values
    - Low chance of collisions
    - All possible values are utilized approximately equally

## Hash Tables
When we need to map an arbitrary data type to another arbitrary data type we opt to use a hash table.
Data is stored in a fixed-sized array, where each data value has a unique index. When we add a new (key, value) pair to the array, we use a hash function to generate a has value within the range of the array with the key. For retrievals we hash the value again and loop up the data in the array at the corresponding index that we get from hashing the value.

When ineveitably collisions occur, we need to consider what to do when hash values collide. One method is using separate chaining where we use a data structure that can dynamically increase in size at each array index and when collision occurs we insert the new value at the index in the dynamic list. Retrievals go through the same step. Another method is called open addressing. Where we use the same table to store everything but we find the next unused space instead when adding a new key.

## Time compolexity
Assuming our hash functions runs in O(1) time then the average time complexity is O(n/k) where n is the number of entries in the hash table and k is the array size of the table (because of the pigenhole principle).
Worst case scenario is when everything in the array is hashed to the same value and that makes the time complexity O(n)
Most modern programming languages have dynamic hash tables which dynamically increase in size depending on the values that we need to store. That makes the average time compolexity O(1) which is very close to accessing an array.

A python dict class is the python equivalent of a hash table.
