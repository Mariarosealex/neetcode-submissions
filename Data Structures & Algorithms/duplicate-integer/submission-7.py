class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group=set()
        for i in nums:
            if i not in group:
                group.add(i)
            else:
                return True
        return False
        