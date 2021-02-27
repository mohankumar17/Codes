class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,arr):
        if len(arr)==0:
            return None
        mid=len(arr)//2
        self.root=TreeNode(arr[mid])
        self.root.left=self.insert(arr[0:mid])
        self.root.right=self.insert(arr[mid+1:])
        return self.root


    def post(self,root):
        if self.root is None:
            return  None
        self.post(self.root.left)
        self.post(self.root.right)
        print(self.root.val,end=' ')

    def levelorder(self,root):
        if self.root is None:
            return None
        q=[]
        q.append(self.root)
        while len(q):
            root=q.pop(0)
            print(root.val,end=' ')
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)



ob=BST()
ar=[1,2,3,4,5]
r=ob.insert(ar)

ob.post(r)
print()
ob.levelorder(r)
