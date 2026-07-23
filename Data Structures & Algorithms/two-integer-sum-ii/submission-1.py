class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for left in range(len(numbers)):
            for right in range(left,len(numbers)):
                if target-numbers[left]==numbers[right]:
                    return [left+1,right+1]
                    
