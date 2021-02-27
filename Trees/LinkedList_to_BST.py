# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree


    def sortedListToBST(self, A):
        if A is None:
            return None
        if A.next is None:
            r=TreeNode(A.val)
            return r

        slow=A
        fast=A.next.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        t=slow.next
        slow.next=None

        root=TreeNode(t.val)
        root.left=self.sortedListToBST(A)
        root.right=self.sortedListToBST(t.next)

        return root
