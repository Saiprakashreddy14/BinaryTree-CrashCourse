class Node:
    def __init__(self,val,right=None,left=None) -> None:
        self.val = val
        self.right = right
        self.left = left
    def __str__(self) -> str:
        return "Node With {} as the Value".format(self.val)

class Solution:

  def preOrder(self,root):
      ans =[] 
      def trsl(root):
        if not root:
            return None
        
        ans.append(root.val) # Node
        trsl(root.left)    # Left
        trsl(root.right)  # Right

        return ans

      trsl(root)
      return ans

  def postOrder(self,root):
      ans =[] 
      def trsl(root):
        if not root:
            return None
        
        
        trsl(root.left)    # Left
        trsl(root.right)  # Right
        ans.append(root.val) # Node

        return ans

      trsl(root)
      return ans

  def inOrder(self,root):
      ans =[] 
      def trsl(root):
        if not root:
            return None

        trsl(root.left)    # Left
        ans.append(root.val) # Node
        trsl(root.right)  # Right

        return ans

      trsl(root)
      return ans



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.left.right = Node(9)



print(Solution().preOrder(root))
print(Solution().postOrder(root))
print(Solution().inOrder(root))

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

    # '''