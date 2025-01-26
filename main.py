class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def add(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.add(val)
        if val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.add(val)
    
    # print tree inorder traversal
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()


    def BST(self, value):
        if self.val == value: # found value
            return True
        elif value < self.val: 
            if self.left is None: # end search or keep moving
                return False
            else:
                return self.left.BST(value)
        else:  # value > self.val 
            if self.right is None: # end search or keep moving
                return False
            else:
                return self.right.BST(value)



# Pre Order First center then left then right return lst
def PreOrder(root):

    def helper(node):
        if node: 
            res.append(node.val)
            helper(node.left)
            helper(node.right)
    res = []
    helper(root)
    return res

def PostOrder(root):
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        res.append(node.val)
    helper(root)
    return res


if  __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(5)
    root.left = TreeNode(1)
    root.add(-10)
    root.add(20)
    root.add(-124)
    root.add(56)
    root.add(-5)
    root.printTree()
    print(root.BST(10))
    print(PreOrder(root))
    print(PostOrder(root))
