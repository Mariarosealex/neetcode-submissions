class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=len(nums)
        final=[]
        for i in range(0,len(nums)):
            product=1
            for j in range(0,i):
                product*=nums[j]
            for j in range(i+1,total):
                product*=nums[j]
            final.append(product)
        return final
