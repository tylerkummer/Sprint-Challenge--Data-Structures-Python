"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True

        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct

        # Check if node has value if not break out
        if self.value is None:
            return

        # If right side of node is empty then its the max value and return it
        if self.right is None:
            return self.value
        # If right side of node is populated then use recursion to re run the function to the next right value
        # repeat process until the right side of node is empty
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Check if node has value if not break out
        if self.value is None:
            return

        # Apply function to the node
        fn(self.value)
        # Apply function the the right of the node if it exists
        if self.right is not None:
            self.right.for_each(fn)
        # Apply function to the left of the node if it exists
        if self.left is not None:
            self.left.for_each(fn)
