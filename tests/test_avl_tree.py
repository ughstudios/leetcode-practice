from trees import AVLTree


def test_avl_tree_insertions() -> None:
    tree = AVLTree()
    tree.recursive_insert(100)
    tree.recursive_insert(105)
    tree.recursive_insert(90)
    tree.recursive_insert(80)
    tree.recursive_insert(70)

    assert tree.root.data == 100
    assert tree.root.right.data == 105
    assert tree.root.left.data == 80
    assert tree.root.left.left.data == 70
    assert tree.root.left.right.data == 90

    tree.delete_tree()
    tree.recursive_insert(100)
    tree.recursive_insert(105)
    tree.recursive_insert(95)
    tree.recursive_insert(97)
    tree.recursive_insert(90)
    assert tree.root.data == 100
    assert tree.root.right.data == 105
    assert tree.root.left.data == 95
    assert tree.root.left.left.data == 90
    assert tree.root.left.right.data == 97

    tree.delete_tree()
    tree.recursive_insert(100)
    tree.recursive_insert(105)
    tree.recursive_insert(86)
    tree.recursive_insert(85)
    tree.recursive_insert(90)
    assert tree.root.data == 100
    assert tree.root.right.data == 105
    assert tree.root.left.data == 86
    assert tree.root.left.right.data == 90
    assert tree.root.left.left.data == 85

    tree.delete_tree()
    tree.recursive_insert(100)
    tree.recursive_insert(90)
    tree.recursive_insert(105)
    tree.recursive_insert(110)
    tree.recursive_insert(106)
    assert tree.root.data == 100
    assert tree.root.left.data == 90
    assert tree.root.right.data == 106
    assert tree.root.right.right.data == 110
    assert tree.root.right.left.data == 105








