class Node:
    def __init__(self,val,right=None,left=None) -> None:
        self.val = val
        self.right = right
        self.left = left
    def __str__(self) -> str:
        return "Node With {} as the Value".format(self.val)

class Solution:
  def rightView(self,root):
    ans = []
    a = []

    def trl(root,level):

      if not root:
        return None
      
      if len(ans)<level:
        ans.append([root.val])
        a.append(root.val)

      trl(root.right,level+1)
      trl(root.left,level+1)

    trl(root,1)
    return a

  def leftView(self,root):
    ans = []
    a = []

    def trl(root,level):

      if not root:
        return None
      
      if len(ans)<level:
        ans.append([root.val])
        a.append(root.val)

      trl(root.left,level+1)
      trl(root.right,level+1)
      

    trl(root,1)
    return a


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.left.right = Node(9)



print(Solution().rightView(root))
print(Solution().leftView(root))

  # ''' Example Tree Representation
    #            1           <---() <<<<<<<-------------
    #          /   \
    #         /     \
    #       2        3
    #      /  \      / \
    #     /    \    /   \
    #    4      5  6     7
    #   /           \
    #  /             \ 
    # 8               9  

    # '''