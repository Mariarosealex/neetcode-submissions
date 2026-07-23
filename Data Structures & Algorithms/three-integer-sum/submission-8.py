class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng=len(nums)
        possibles=[]
        s=sorted(nums)
        for i in range(leng-2):
            left=i+1
            right=leng-1
            target=-s[i]
            if i>0 and s[i]==s[i-1]:
                continue
            while left<right:
                curr_sum=s[left]+s[right]
                if curr_sum==target:
                    possibles.append([s[i],s[left],s[right]])
                    left+=1
                    right-=1
                    while left<right and s[left]==s[left-1]:
                        left+=1
                    while left<right and s[right]==s[right+1]:
                        right-=1
                    continue
                elif curr_sum>target:
                    right-=1
                else:
                    left+=1
        return possibles
                