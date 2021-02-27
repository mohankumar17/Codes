#######################################################
def util(root,level,maxLevel,ans):
    if root is None:
        return None
    if level>maxLevel[0]:
        ans.append(root.data)
        maxLevel[0]=level

    util(root.left,level+1,maxLevel,ans)
    util(root.right,level+1,maxLevel,ans)

def LeftView(root):
    ans=[]
    maxLevel=[0]
    util(root,1,maxLevel,ans)
    return ans
#######################################################

def util(root,level,maxLevel,ans):
    if root is None:
        return None
    if level>maxLevel[0]:
        ans.append(root.data)
        maxLevel[0]=level

    util(root.right,level+1,maxLevel,ans)
    util(root.left,level+1,maxLevel,ans)


def rightView(root):
    ans=[]
    maxLevel=[0]
    util(root,1,maxLevel,ans)
    return ans
#######################################################


#######################################################


#######################################################
