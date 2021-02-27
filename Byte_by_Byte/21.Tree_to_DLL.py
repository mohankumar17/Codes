'''
def DLL2(root,head):
    if root is None:
        return head
    DLL2(root.right,head)
    root.right=head
    if head is not None:
        head.left=root
    head=root
    DLL2(root.left,head)
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def DLL(root):
    def DLL2(root):
        if root is None:
            return None
        DLL2(root.left)
        l.append(root)
        DLL2(root.right)
    l=[]
    DLL2(root)
    #############################
    node=l[0]
    node.left=None
    head=node
    for i in range(1,len(l)):
        node.right=l[i]
        x=node
        node=node.right
        node.left=x
    return head


ob=Tree()
ob.root=TreeNode(1)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(3)
ob.root.left.left=TreeNode(4)
ob.root.left.right=TreeNode(5)
ob.root.right.left=TreeNode(6)
ob.root.right.right=TreeNode(7)

head=DLL(ob.root)

while head.right is not None:
    print(head.val,end=' ')
    head=head.right
print(head.val)
print()
tail=head
while tail is not None:
    print(tail.val,end=' ')
    tail=tail.left
