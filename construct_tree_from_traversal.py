# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional
from utils import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or inorder:
        return None
    
    root = TreeNode(preorder[0])
    # this is the middle because inorder is: left, root, right. 
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1: mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root
