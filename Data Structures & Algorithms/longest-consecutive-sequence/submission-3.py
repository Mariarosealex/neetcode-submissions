class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=sorted(nums)
        leng=1
        best_len=1
        if len(num)==0:
            return 0
        for i in range(len(num)-1):
            if num[i]+1==num[i+1]:
                leng+=1
            elif num[i]==num[i+1]:
                leng=leng+0
            else:                
                leng=1
            best_len=max(leng, best_len)  
            
        return best_len