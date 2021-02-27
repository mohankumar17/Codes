class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        n=Node(data)
        if self.root is None:
            self.root=n
        else:
            curr=self.root
            while True:
                if data<curr.data:
                    if curr.left is None:
                        curr.left=n
                        break
                    else:
                        curr=curr.left

                elif data>curr.data:
                    if curr.right is None:
                        curr.right=n
                        break
                    else:
                        curr=curr.right
                else:
                    break

#####################
def Distance_from_root(root,x):
    if root.data==x:
        return 0
    if x<root.data:
        return 1+Distance_from_root(root.left,x)
    return 1+Distance_from_root(root.right,x)

def DistanceUtil(root,x,y):
    if root is None:
        return 0
    if x<root.data and y<root.data:
        return DistanceUtil(root.left,x,y)
    if x>root.data and y>root.data:
        return DistanceUtil(root.right,x,y)

    if x<=root.data and y>=root.data:
        return Distance_from_root(root,x)+Distance_from_root(root,y)


def Distance(root,x,y):
    if x>y:
        x,y=y,x
    return DistanceUtil(root,x,y)


ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)

x=int(input())
y=int(input())
print(Distance(ob.root,x,y))
