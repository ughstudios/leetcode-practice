# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://stackoverflow.com/questions/32543608/deque-popleft-and-list-pop0-is-there-performance-difference
from typing import Optional
from utils import TreeNode
from collections import deque

def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

