class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group={}
        for i in range(len(nums)):
            if nums[i] not in group:
                group[nums[i]]=i
            else:
                return True
        return False
        