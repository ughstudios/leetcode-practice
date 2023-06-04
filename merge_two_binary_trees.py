# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional
from utils import TreeNode


def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
        return None

    v1 = root1.value if root1 else 0
    v2 = root2.value if root2 else 0
    root = TreeNode(v1 + v2)

    root.left = merge_trees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = merge_trees(root1.right if root1 else None, root2.right if root2 else None)
    return root
