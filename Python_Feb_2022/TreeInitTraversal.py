# tree traversal Algorithms
class Node:
    def __init__(self,val):
        self.childleft=None
        self.childright=None
        self.nodedata=val
def InOdr(root):#L+R
    if root:
        InOdr(root.childleft)
        print(root.nodedata,end=" ")
        InOdr(root.childright)
def PreOrd(root):#+LR
    if root:
        print(root.nodedata,end=" ")
        PreOrd(root.childleft)
        PreOrd(root.childright)
def PostOrd(root):#LR+
    if root:
        PostOrd(root.childleft)
        PostOrd(root.childright)
        print(root.nodedata,end=" ")
root=Node(1)
root.childleft=Node(2)
root.childright=Node(3)
root.childleft.childleft=Node(4)
root.childleft.childright=Node(5)
InOdr(root)
print("\n")
PreOrd(root)
print("\n")
PostOrd(root)

