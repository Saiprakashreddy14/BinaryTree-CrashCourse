class Node:
    def __init__(self,val,right=None,left=None) -> None:
        self.val = val
        self.right = right
        self.left = left
    def __str__(self) -> str:
        return "Node With {} as the Value".format(self.val)

class Solution:
  def heightofBT(self,root):

    if not root:
      return 0 

    lh = self.heightofBT(root.left )
    rh = self.heightofBT(root.right)

    return 1 + max(lh,rh)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.left.right = Node(9)
root.right.left.right.left = Node(10)

print(Solution().heightofBT(root))

  # ''' Example Tree Representation
    #            1
    #          /   \
    #         /     \
    #       2        3
    #      /  \      / \
    #     /    \    /   \
    #    4      5  6     7
    #   /           \
    #  /             \ 
    # 8               9  
    #                   /
    #                  /
    #                 10  
    # # '''