class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       group=[]
       for num in nums:
            if num in group:
                return True
            else:
                group.append(num)
       return False