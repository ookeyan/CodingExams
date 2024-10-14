
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #if the root is None. If it is, return None
            return
            
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root #return the current node (root)
#root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)

def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Helper function to print the tree in level-order (for testing purposes)
def printTree(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Test the invertTree function
s = Solution()

# Test case 1
root = buildTree([4, 2, 7, 1, 3, 6, 9])
inverted_root = s.invertTree(root)
print(printTree(inverted_root))  # Expected output: [4, 7, 2, 9, 6, 3, 1]

# Test case 2
root = buildTree([2, 1, 3])
inverted_root = s.invertTree(root)
print(printTree(inverted_root))  # Expected output: [2, 3, 1]

# Test case 3 (Empty tree)
root = buildTree([])
inverted_root = s.invertTree(root)
print(printTree(inverted_root))  # Expected output: []
