'''
GeneralTree -> a node can have any number of elements
BinaryTree -> a node can have only two number of elements
BinarySearchTree -> is a binary tree with a specific order,where left node is all the elements which are less than it's parent,and right node's element are greater than its parent
'''


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node data already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                # coudn't find
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                # coudn't find
                return False

    def post_order_traversal(self):
        elements = []

        # left
        if self.left:
            elements += self.left.post_order_traversal()

        # right
        if self.right:
            elements += self.right.post_order_traversal()

        # center
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # center
        elements.append(self.data)

        # left
        if self.left:
            elements += self.left.post_order_traversal()

        # right
        if self.right:
            elements += self.right.post_order_traversal()

        return elements

    def in_order_traversal(self):
        elements = []

        # left
        if self.left:
            elements += self.left.in_order_traversal()

        # center
        elements.append(self.data)

        # right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.right == None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()

    def calcuate_sum(self):
        left_sum = self.left.calcuate_sum() if self.left else 0
        right_sum = self.right.calcuate_sum() if self.right else 0

        return self.data + left_sum + right_sum
    '''
        to delete a node if it is a leaf node it is simple.
        but if it is a branch node there is two ways to do it
            {
                1. -> copy least data from its right node and delete the duplicate one
                2. -> copy biggest data from its left node and delete the duplicate one
            }
    '''

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            # else:
            #     return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left == None and self.right == None:
                return None

            if self.left == None:
                return self.right

            if self.right == None:
                return self.left

            # now i have both right and left values
            '''
            we are using method no. 1.
            '''
            min_val = self.right.find_min()
            self.data = min_val
            # make current node's right child node the found node
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [1, 2, 32, 442, 21, 22, 34]

    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(26))
    numbers_tree.delete(2)
    print(numbers_tree.in_order_traversal())

    # it works with string aswell
