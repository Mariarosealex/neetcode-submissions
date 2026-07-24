class Solution:
    def trap(self, height: List[int]) -> int:
        max_area=0
        maxleft=0
        maxright=0
        left=0
        right=len(height)-1
        for i in range(1,len(height)-1):
            while left<i:
                maxleft=max(height[left],maxleft)
                left+=1
            left=0
            
            while right>i:
                maxright=max(height[right],maxright)
                right-=1
            
            right=len(height)-1
            water=max(min(maxleft,maxright)-height[i],0)
            max_area+=water
            maxleft=0
            maxright=0
        return max_area
