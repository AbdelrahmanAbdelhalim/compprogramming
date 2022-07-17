# Sorting
Sorting is one of the most fundamental algorithms in computer science.
Stable sorting algorithms means that their relative order is maintained when two elements have the same value. For example in a deck of cards if we have the 7 of hearts before the 7 of spades in the initial hand, after a stable sort, the 7 of hearts is still before the 7 of spades. In an unstable algorithm the order can change their positions.

## Insertion sort
We start with the initial item and consider it sorted. Then for each subsequent element we insert that element in the sorted list by swapping it until it is in the correct postion relative to the current number.

## Selection sort
In selection sort we have a temporary variable keeping track of the index of the smallest element. We then update that index if necessary (We found an element smaller than that the index points to). After all comparisons are done we swap the smallest index with the first index of the sorted pile. Note: the sorted pile here is not necessarily a brand new array. The sorted pile can be considered to be the elements at index 0 in the array up to how many elements we have sorted so far.
Overall time complexity is O(n * (n + 1) / 2) which is equivalent to O(n^2)

## Bubble sort
The idea of bubble sort is that the biggest item floats up the array. For each cycle of the array we compare the element to the one next to it. We swap the elements if needed. If not we don't swap and continue the loop. Efficively taking the next element in consideration (the bigger one). This way for each cycle the biggest elements start to bubble up to the top. From here we can see that the list will be guranteed to be sorted in n passes. It is a STABLE sorting algorithm because it would not move a number past one with the same value.
Overall time complexity = O( n ^ 2)

# Advanced Sorting Algorithms:

# Merge Sort
A divide and conquer algorithm. Works by dividing the unsorted list in half and then merging them up again (and sorting them as we merge). To merge we have to pointers point to the first indices of the two lists we are trying to merge. And for we start adding the smallest element to a list and pushing the pointer by 1 for the list we added the item from. We continue to do this until both lists are fully added or we fully have added one of the lists in the sorted pile.

Overall time complexity: O(nlog(n))

# Quick Sort
Idea of quick sort is: selecting an arbitrary pivot and then putting values less than it on one side and values larger than it on the other side. After grouping them this way we swap the pivot with the first element on the side that is larger or equal to the pivot. Then we need to sort the left and right intervals using the same method, then the list will be sorted.

How would it group? One of the ways to achieve this is that for the interval that we are sorting, we have a pointer point before the start and at the end (including the pivot). For each swap, we move the start pointer until we find an element larger or equal to the pivot (after the initial index) and move the end pointer until we find an element smaller or equal to the pivot (before the initial index). Then we can swap those two elements and restart the process. If those two pointers meet, we stop , and then we can swap the pivot and the meeting point.

Time complexity of quick sort is O(nlog(n)) on average. However, in the worst case scenario, each interval to sort is one less than the current interval. Which would make the time complexity O(n^2). This depends heavily on the pivot you choose. If you choose the largest value as the pivot every time you would reach that time complexity. However, the chances of that happening is very low. It sorts the array in place. However, that doesn't mean that the space complexity is constant, it uses recursion as its core logic, and the minimum recursion layers are equal to log(n).

# Built in Sorting Algorithms
## Python
You can use list.sort() and sorted(list) to return a new list that is sorted. Both are stable. Python uses Timsort that uses merge sort for larger data structures and insertion sort for smaller ones.
## Java
In java you can use Arrays.sort(array) or Collections.sort(list) to sort a java list. They are both stable. Java uses a version of Timsort that allows faster sorting for partially sorted data.
