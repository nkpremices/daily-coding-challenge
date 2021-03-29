##### This problem was asked by WeWork.

# Challenge 6

### Question

You are given an array of integers representing coin denominations and a total amount of money.
Write a function to compute the fewest number of coins needed to make up that amount. 
If it is not possible to make that amount, return null.

For example, given an array of `[1, 5, 10]` and an amount `56`, return `7` since we can use 5 dimes, 1 nickel, and 1 penny.

### Solution

* Store the total number of available coins
* Declare a 2-D list, filled with zeroes
* Initialise first column of list with 0 because a sum of 0 can be made with zero coins
* Initialise first row of list with +ve infinity because a sum cannot be made with 0 coins
* Use recursive solution
