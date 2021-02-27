import random
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def nodes(self):
        q=[self.root]
        self.r=[]
        while len(q):
            x=q.pop(0)
            self.r.append(x)
            if x.left is not None:
                q.append(x.left)
            if x.right is not None:
                q.append(x.right)

    def getRandomNode(self):
        return random.choice(self.r)

ob=Tree()
ob.root=TreeNode(5)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(7)
ob.root.left.left=TreeNode(1)
ob.root.left.right=TreeNode(3)
ob.root.right.left=TreeNode(6)
ob.root.right.right=TreeNode(8)
ob.nodes()
print(ob.getRandomNode().val)
print(ob.getRandomNode().val)
print(ob.getRandomNode().val)
print(ob.getRandomNode().val)
