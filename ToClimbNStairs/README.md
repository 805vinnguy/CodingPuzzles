# To Climb N Stairs

## Puzzle
There exists a staircase with N steps, and you can climb 1 or 2 steps at a time.  Given N, write a function that returns the number of unique ways you can climb the staircase.  The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
+ 1, 1, 1, 1
+ 2, 1, 1
+ 1, 2, 1
+ 1, 1, 2
+ 2, 2

Bonus: What if instead of being able to climb 1 or 2 steps at a time, you could climb any number of steps from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

## Approach

### Known
+ For either puzzle or bonus puzzle, you are limited to movement by 1 or 2 steps, and steps present in the set X, respectively.
+ The sum of all of you individual step choices sum up to N.
+ For the regular puzzle, you can generalize the 1 or 2 step movement into the bonus puzzle with a set X = {1, 2}.
+ The puzzle is an exhaustive search.
+ There exists sets of X where N is unreachable.
+ N is reachable from a node if the steps remaining are equal to an available step choice or equal to a multiple of an available step choice.

### Parameters
+ N : number of steps in the staircase
+ X : set of valid steps you may take

### Ideas
1. I am thinking a tree traversal of some sort where all of leaf nodes contain the sum of the path to them. Those equivalent to N are counted.  Start the root at 0.
