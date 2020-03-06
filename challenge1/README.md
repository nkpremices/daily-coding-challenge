##### This problem was recently asked by Google.

# Challenge 1

### Question
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

### Solution

* Loop once though the store storing each element in a loop variable
* Loop the second time within the first loop comparing the sum of the first loop variable with the second one if it adds up to the provided key
* Test all the possible cases within the second loop and break the loop only when the sum adds up to the key
* Return False by default

