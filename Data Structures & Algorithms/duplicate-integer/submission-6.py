class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group=set()
        for i in range(len(nums)):
            if nums[i] not in group:
                group.add(nums[i])
            else:
                return True
        return False
        