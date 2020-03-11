##### This problem was asked by Google.

# Challenge 3

### Question

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:

```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
### Solution

The secret here is to define the data structure that you are going to use when serializing. In this demo, I will use dictionaries

* create a method called `__str__` in the Node class and make sure it uses recursion in the sense that what it returns calls also the `__str__` method on the members of the class
* Use the json module to stringify the objects of the class. This will ensure an easy loading when deserializing

* create the serialize method and implement the exact same thing implemented in the `__str__` method. This will ensure the recursion
* Create the deserialize method. make sure that it calls the `loads` method of `json` and that for each child of the dictionary it checks the type and calls itself in case the type is a dictionary
 
