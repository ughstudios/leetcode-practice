""" Tests for binary tree implementation """
from trees import BinaryTree


def test_binary_tree():
    tree = BinaryTree()

    test_data = [1, 2, 3, 4, 5, 'test']
    for data in test_data:
        tree.insert(data)
        assert tree.search(data)
        tree.delete(data)
        assert not tree.search(data)

    tree.insert('pizza')
    tree.insert('pie')
    tree.insert('chicken')
    tree.insert('cheese')
    tree.insert('tacos')
    tree.delete('tacos')
    deepest_node = tree.get_deepest_node()
    assert deepest_node.data == 'cheese'
