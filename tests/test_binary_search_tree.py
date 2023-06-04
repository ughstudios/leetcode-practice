""" Tests for binary search tree implementation """
from trees import BinarySearchTree, get_tree_height_recursively, get_tree_height_iteratively


def check_tree_size(expected_size: int, tree: BinarySearchTree) -> None:
    assert get_tree_height_iteratively(tree.root) == expected_size
    assert get_tree_height_recursively(tree.root) == expected_size


def insert_test_data_into_tree(tree: BinarySearchTree, test_data: list[int]) -> None:
    for data in test_data:
        tree.insert(data)


def test_binary_search_tree():
    tree = BinarySearchTree()
    test_data = (1, 2, 3, 10, 9, 100, 1500)
    insert_test_data_into_tree(tree, test_data)
    assert tree.root.data == test_data[0]
    assert tree.root.right.data == test_data[1]
    assert tree.root.right.right.data == test_data[2]
    assert tree.root.right.right.right.data == test_data[3]
    assert tree.root.right.right.right.left.data == test_data[4]
    assert tree.root.right.right.right.right.data == test_data[5]
    assert tree.root.right.right.right.right.right.data == test_data[6]

    tree.delete_tree()
    tree.insert(500)
    check_tree_size(1, tree)
    tree.insert(501)
    check_tree_size(2, tree)
    tree.insert(502)
    check_tree_size(3, tree)
    tree.insert(499)
    check_tree_size(3, tree)
    tree.delete_recursive(499)
    tree.insert(499)
    tree.delete_iterative(499)
    check_tree_size(3, tree)
    tree.insert(499)
    tree.delete_recursive(499)
    check_tree_size(3, tree)

    check_tree_size(3, tree)
    tree.delete_recursive(502)
    check_tree_size(2, tree)
    tree.delete_recursive(500)
    check_tree_size(1, tree)
    tree.delete_tree()
    check_tree_size(0, tree)

    tree.delete_tree()
    test_data2 = (500, 490, 485, 495, 510)
    insert_test_data_into_tree(tree, test_data2)

    tree.delete_recursive(490)
    check_tree_size(3, tree)
    assert not tree.search(490)
    tree.delete_recursive(500)
    assert not tree.search(500)
    assert tree.search(485)
    assert tree.search(495)
    assert tree.search(510)
