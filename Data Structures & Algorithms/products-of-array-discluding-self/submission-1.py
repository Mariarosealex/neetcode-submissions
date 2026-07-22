class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=len(nums)
        product=[]
        left=[]
        right=[1]*total
        left.append(1)
        value=1
        num=1
        for i in range(1,total):
            value*=nums[i-1]
            left.append(value)
        for i in range(total-1,0,-1):
            num*=nums[i]
            right[i-1]=num
        for i in range(total):
            product.append(left[i]*right[i])
        return product
            