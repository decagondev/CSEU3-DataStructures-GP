# create a Node Class
class Node:
    def __init__(self, value=None, next_node=None):
        # set the initial value of our node
        self.value = value

        # set a ref to the next node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node



    