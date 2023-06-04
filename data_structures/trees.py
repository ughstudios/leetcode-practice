""" This module implements multiple types of trees """
from __future__ import annotations
from typing import Any, Optional
from my_queue import Queue


class TreeNode:
    """ Base tree node used for all binary trees """
    def __init__(self, data: Any):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


class BasicTree:
    """ Basic Tree with array of children """
    def __init__(self):
        self.children = []
        self.data = None

    def add_child(self, value: Any) -> None:
        """ Adds a child to the tree """
        node = TreeNode(value)
        self.children.append(node)


def get_tree_height_recursively(root: TreeNode) -> int:
    """ Returns the height of a tree, or subtree from a given root (uses recursion) """
    if not root:
        return 0
    left_height = get_tree_height_recursively(root.left)
    right_height = get_tree_height_recursively(root.right)
    return max(left_height, right_height) + 1


def get_tree_height_iteratively(root: TreeNode) -> int:
    """ Returns the height of a tree, or subtree from a given root (uses an iterative approach) """
    if not root:
        return 0

    my_queue = Queue()
    my_queue.enqueue(root)
    left_height = 0
    right_height = 0
    while not my_queue.is_empty():
        node = my_queue.dequeue()
        if node.left:
            left_height += 1
            my_queue.enqueue(node.left)
        if node.right:
            right_height += 1
            my_queue.enqueue(node.right)
    return max(left_height, right_height) + 1


class BinaryTree:
    """ Basic Binary Tree """
    def __init__(self):
        self.root = None

    def search(self, value: Any) -> bool:
        """ Searches for a value in the binary tree, returns true if it exists """
        if self.root and self.root.data == value:
            return True

        my_queue = Queue()
        my_queue.enqueue(self.root)
        while not my_queue.is_empty():
            node = my_queue.dequeue()
            if node and node.data == value:
                return True
            else:
                if node and node.left:
                    my_queue.enqueue(node.left)
                if node and node.right:
                    my_queue.enqueue(node.right)
        return False

    def insert(self, value: Any) -> None:
        """ Inserts a new value into the binary tree """
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            my_queue = Queue()
            my_queue.enqueue(self.root)
            while not my_queue.is_empty():
                node = my_queue.dequeue()
                if not node.left:
                    node.left = new_node
                    break
                if not node.right:
                    node.right = new_node
                    break
                if node.left:
                    my_queue.enqueue(node.left)
                if node.right:
                    my_queue.enqueue(node.right)

    def is_empty(self) -> bool:
        """ Returns true if the tree is empty """
        return not self.root

    def get_deepest_node(self) -> Optional[TreeNode]:
        """ Gets the deepest node from a level order traversal """
        if not self.root:
            return
        else:
            my_queue = Queue()
            my_queue.enqueue(self.root)
            temp = None
            while not my_queue.is_empty():
                temp = my_queue.dequeue()
                if temp.left:
                    my_queue.enqueue(temp.left)
                if temp.right:
                    my_queue.enqueue(temp.right)
            return temp

    def delete_deepest_node(self, deepest_node: TreeNode) -> None:
        """ Deletes the deepest node in the binary tree """
        if not self.root:
            return
        else:
            my_queue = Queue()
            my_queue.enqueue(self.root)
            while not my_queue.is_empty():
                temp = my_queue.dequeue()
                if temp.left == deepest_node:
                    temp.left = None
                    break
                if temp.right == deepest_node:
                    temp.right = None
                    break

                my_queue.enqueue(temp.left)
                my_queue.enqueue(temp.right)

    def delete(self, value: Any) -> None:
        """ Deletes the first instance of a value """
        if self.root.data == value:
            self.root = self.root.left
            return

        my_queue = Queue()
        my_queue.enqueue(self.root)
        while not my_queue.is_empty():
            node = my_queue.dequeue()
            if node.left and node.left.data == value:
                deepest_node = self.get_deepest_node()
                if node.left == deepest_node:
                    node.left = None
                else:
                    node.left = deepest_node
                    self.delete_deepest_node(deepest_node)
                break
            if node.right and node.right.data == value:
                deepest_node = self.get_deepest_node()
                if node.right == deepest_node:
                    node.right = None
                else:
                    node.right = deepest_node
                    self.delete_deepest_node(deepest_node)
                break

            if node.left:
                my_queue.enqueue(node.left)
            if node.right:
                my_queue.enqueue(node.right)


def min_value_node(root: TreeNode) -> TreeNode:
    """ Returns the minimum value node in the binary search tree (in order successor) """
    temp = root
    while temp and temp.left:
        temp = temp.left
    return temp


def max_value_node(root: TreeNode) -> TreeNode:
    """ Returns the maximum value node in the binary search tree (in order predecessor) """
    temp = root
    while temp and temp.right:
        temp = temp.right
    return temp


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree implementation
    Properties of Binary Search tree:
        All values to the left of a root must be lower than that root's right value
        All values must be unique
        There may only be two children of any node, left and right.
    Wikipedia: https://en.wikipedia.org/wiki/Binary_search_tree
    """

    def __init__(self):
        super().__init__()
        self.list_of_unique_values = set()
        self.inorder_successor = min_value_node

    def insert(self, value: int) -> None:
        """ Insert non-duplicate values into a binary search tree. The set is used for checking for duplicates """
        if value not in self.list_of_unique_values:
            self.list_of_unique_values.add(value)
        elif value in self.list_of_unique_values:
            return

        if not self.root:
            self.root = TreeNode(value)
        else:
            my_queue = Queue()
            my_queue.enqueue(self.root)
            while not my_queue.is_empty():
                node = my_queue.dequeue()
                if value >= node.data:
                    if not node.right:
                        node.right = TreeNode(value)
                    elif node.right:
                        my_queue.enqueue(node.right)
                elif value <= node.data:
                    if not node.left:
                        node.left = TreeNode(value)
                    elif node.left:
                        my_queue.enqueue(node.left)

    def recursive_insert_helper(self, root: TreeNode, value: int) -> None:
        """ Helper function for recursive_insert method """
        if value >= root.data:
            if not root.right:
                root.right = TreeNode(value)
                return
            else:
                self.recursive_insert_helper(root.right, value)
        elif value <= root.data:
            if not root.left:
                root.left = TreeNode(value)
                return
            else:
                self.recursive_insert_helper(root.left, value)

    def recursive_insert(self, value: int) -> None:
        """ Recursively inserts a value into the binary search tree """
        self.recursive_insert_helper(self.root, value)

    def delete_tree(self) -> None:
        """ Deletes the entire tree """
        self.root = None
        self.list_of_unique_values = set()

    def search(self, value: int) -> bool:
        """ Searches for a value in BST, if it exists returns True """
        if self.root and self.root.data == value:
            return True
        node = self.root
        while node:
            if node.data == value:
                return True
            if value > node.data:
                node = node.right
            elif value < node.data:
                node = node.left
        return False

    def delete_recursive_helper(self, root: TreeNode, value: int) -> Optional[TreeNode]:
        """ Recursive helper method for deleting a value from a BST """
        if not root:
            return root

        if value < root.data:
            root.left = self.delete_recursive_helper(root.left, value)
        elif value > root.data:
            root.right = self.delete_recursive_helper(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find inorder successor, we have two children on this node
            # We want to find the lowest node that has a value higher than the value we are trying to delete
            # So if we move to the right once, we will be in a subtree where all values are higher than our current
            # root. Then we want to find the lowest value in this subtree.
            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete_recursive_helper(root.right, root.data)
        return root

    def delete_recursive(self, value: int) -> None:
        """ Deletes a value from the BST using a recursive approach """
        self.root = self.delete_recursive_helper(self.root, value)

    def delete_iterative(self, value: int) -> None:
        """ Delete a value from the BST using an iterative approach. """
        # Parent points to the parent of the node to be deleted.
        current = self.root
        parent = None
        while current and current.data != value:
            parent = current
            if value > current.data:
                current = current.right
            else:
                current = current.left

        # If current is None, then the value doesn't exist in the bst.
        if not current:
            return

        # If the node to be deleted has no children.
        if not current.left and not current.right:
            # If it's the root and it has no children, just delete the root.
            if current == self.root:
                self.root = None
            elif parent.left == current:
                parent.left = None
                return
            elif parent.right == current:
                parent.right = None
                return

        # If the node has one child
        if not current.left or not current.right:
            if not current.left:
                new_curr = current.right
            else:
                new_curr = current.left

            # If the value to be deleted is the root.
            if not parent:
                self.root = new_curr
                return

            if current == parent.left:
                parent.left = new_curr
            else:
                parent.right = new_curr

        # If the node has two children
        if current.left and current.right:
            temp_parent = None

            temp = current.right
            # Find the inorder successor of the current node (the one we want to delete)
            while temp.left:
                temp_parent = temp
                temp = temp.left

            if temp_parent:
                temp_parent.left = temp.right
            else:
                current.right = temp.right

            current.data = temp.data
        self.list_of_unique_values.remove(value)


def _avl_get_tree_height(node: TreeNode) -> int:
    """ Gets the height of a subtree node in an AVL Tree """
    if not node:
        return 0
    return node.height


def _avl_get_balance(root: TreeNode):
    """ Gets the difference of height between the left and right subtrees of a tree node. """
    if not root:
        return 0
    return _avl_get_tree_height(root.left) - _avl_get_tree_height(root.right)


def _avl_rotate_right(imbalanced_node: TreeNode) -> TreeNode:
    """ Performs a Right Rotation on a tree node given the imbalanced node """
    new_root = imbalanced_node.left
    imbalanced_node.left = imbalanced_node.left.right
    new_root.right = imbalanced_node
    # Modify heights
    imbalanced_node.height = 1 + max(_avl_get_tree_height(imbalanced_node.left),
                                     _avl_get_tree_height(imbalanced_node.right))
    new_root.height = 1 + max(_avl_get_tree_height(new_root.left), _avl_get_tree_height(new_root.right))
    return new_root


def _avl_rotate_left(imbalanced_node: TreeNode) -> TreeNode:
    """ Performs a Left Rotation on a tree node given the imbalanced node """
    new_root = imbalanced_node.right
    imbalanced_node.right = imbalanced_node.right.left
    new_root.left = imbalanced_node
    # Modify heights
    imbalanced_node.height = 1 + max(_avl_get_tree_height(imbalanced_node.left),
                                     _avl_get_tree_height(imbalanced_node.right))
    new_root.height = 1 + max(_avl_get_tree_height(new_root.left), _avl_get_tree_height(new_root.right))
    return new_root


class AVLTree(BinarySearchTree):
    """ Implementation of an AVL Tree """
    def recursive_insert_helper(self, root: TreeNode, value: int) -> TreeNode:
        """ Helper method for recursive_insert method """
        if not root:
            return TreeNode(value)
        elif value > root.data:
            root.right = self.recursive_insert_helper(root.right, value)
        elif value < root.data:
            root.left = self.recursive_insert_helper(root.left, value)

        root.height = 1 + max(_avl_get_tree_height(root.left), _avl_get_tree_height(root.right))
        balance = _avl_get_balance(root)
        # Left, left condition
        if balance > 1 and value < root.left.data:
            return _avl_rotate_right(root)
        # Left, right condition
        if balance > 1 and value > root.left.data:
            root.left = _avl_rotate_left(root.left)
            return _avl_rotate_right(root)
        # Right, right condition
        if balance < -1 and value > root.right.data:
            return _avl_rotate_left(root)
        # Right, left condition
        if balance < -1 and value < root.right.data:
            root.right = _avl_rotate_right(root.right)
            return _avl_rotate_left(root)

        return root

    def recursive_insert(self, value: int) -> None:
        """ Implementation of insertion method using recursion in an AVL Tree """
        self.root = self.recursive_insert_helper(self.root, value)

    def delete_recursive_helper(self, root: TreeNode, value: int) -> Optional[TreeNode]:
        """" Helper method for delete_recursive method """
        if not root:
            return None
        elif value > root.data:
            root.right = self.delete_recursive_helper(root.right, value)
        elif value < root.data:
            root.left = self.delete_recursive_helper(root.left, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete_recursive_helper(root.right, temp.data)
        root.height = 1 + max(_avl_get_tree_height(root.left), _avl_get_tree_height(root.right))
        balance = _avl_get_balance(root)
        # Left, left
        if balance > 1 and _avl_get_balance(root.left) >= 0:
            return _avl_rotate_right(root)
        # Right, right
        if balance < -1 and _avl_get_balance(root.right) <= 0:
            return _avl_rotate_left(root)
        # Left, right
        if balance > 1 and _avl_get_balance(root.left) < 0:
            root.left = _avl_rotate_left(root.left)
            return _avl_rotate_right(root)
        # Right, left
        if balance < -1 and _avl_get_balance(root.right) > 0:
            root.right = _avl_rotate_right(root.right)
            return _avl_rotate_left(root)

        return root

    def delete_recursive(self, value: int) -> None:
        """ Implementation of deleting a value from an AVL Tree """
        self.root = self.delete_recursive_helper(self.root, value)
