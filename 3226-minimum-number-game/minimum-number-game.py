class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        while len(nums)!=0:
            mini=min(nums)
            
            nums.remove(mini)

            minim=min(nums)

            arr.append(minim)
            arr.append(mini)
            nums.remove(minim)
        return arr

        