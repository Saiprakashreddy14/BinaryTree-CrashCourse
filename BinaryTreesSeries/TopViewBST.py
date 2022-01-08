class Node:
    def __init__(self,val,right=None,left=None) -> None:
        self.val = val
        self.right = right
        self.left = left
    def __str__(self) -> str:
        return "Node With {} as the Value".format(self.val)

class Solution:
    def topView(self,root):
      def sol(root,lvl,zone,d):
        if not root:
          return None
        
        if zone not in d:
          d[zone]=root.val

        sol(root.left,lvl+1,zone-1,d)
        sol(root.right,lvl+1,zone+1,d)

        return d

      dic = sol(root,1,0,{})
      ans = []
      for i in sorted(dic):
        ans.append(dic[i])

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


print(Node)

print(Solution().topView(root))

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