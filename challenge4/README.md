##### This problem was asked by Stripe.

# Challenge 4

### Question

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give 2. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.

### Solution

* get rid of all negative numbers then sort the list
* create a list full of all integer up to the highest
* Return the highest + 1 if the length is the same
* Otherwise, find the difference then sort it
* Return the first item of the difference
