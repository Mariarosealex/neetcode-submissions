class Solution:
    def trap(self, height: List[int]) -> int:
        max_area=0
        maxleft=[]
        maxright=[0]*len(height)
        maxleft.append(height[0])
        maxright[len(height)-1]=height[len(height)-1]
        for i in range(1,len(height)):
            maxleft.append(max(maxleft[i-1],height[i]))
        for i in range(len(height)-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i])
        for i in range(len(height)):
            water=max(min(maxleft[i],maxright[i])-height[i],0)
            max_area+=water
        return max_area
