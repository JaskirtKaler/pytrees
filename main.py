class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def add(self, val):
        if val < root.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.add(val)
        if val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.add(val)
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()
if  __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(5)
    root.left = TreeNode(1)
    root.add(-10)
    print("Sample")
    root.printTree()