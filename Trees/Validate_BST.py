def checkBST(root,l,r):
    if root is None:
        return True
    if l is not None:
        if l.data>=root.data:
            return False
    if r is not None:
        if r.data<=root.data:
            return False
    return checkBST(root.left,l,root) and checkBST(root.right,root,r)



print(checkBST(root,None,None))
