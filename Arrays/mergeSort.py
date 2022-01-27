class Solution:
    def __init__(self) -> None:
        pass
    def mergesort(self,arr):

        if len(arr)<2:
            return arr

        m = len(arr)//2

        lft = self.mergesort(arr[:m])
        rgt = self.mergesort(arr[m:])

        i,j,k = 0,0,0

        while i<len(lft) and j<len(rgt) :
            if lft[i]<rgt[j]:
                arr[k]=lft[i]
                i+=1
            elif lft[i]>rgt[j]:
                arr[k]=rgt[j]
                j+=1
            k+=1
            
        while i < len(lft):
            arr[k] = lft[i]
            i += 1
            k += 1

        while j < len(rgt):
            arr[k]=rgt[j]
            j += 1
            k += 1
        
        print(lft,rgt,arr)

        return arr

arr = [5,3,2,4,1]
print(Solution().mergesort(arr))