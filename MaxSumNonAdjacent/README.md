# Max Sum Non Adjacent

## Puzzle
+ Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 and negative.
+ For example, [2, 4, 6, 2, 5,] should return 13, since we pick 2, 6, and 5.
+ [5, 1, 1, 5] should return 10, since we pick 5 and 5.
+ Bonus: Can you do this in O(n) time and constant space?

## Approach
+ Dynamic Programming
    + Have two variables:
        + one holding the largest sum accumulated including the last element seen
        + one holding the largest sum accumulated excluding the last element seen
