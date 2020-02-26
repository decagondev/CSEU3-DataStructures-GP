import sys
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
            # does it have a child to the left?
                # place our new node here
            # otherwise
                # repeat process for the left

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
            # does it have a child to the right?
                # place our new node here
            # otherwise
                # repeat the process for the right

        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE

        # LEFT CASE

        # RIGHT CASE

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree
            # return none

        # recursive case
        # if there is no right value 
            # return the root node value
        # otherwise
            # return get max of the right hand child
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass