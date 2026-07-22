class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        for i in nums:
            if i not in group:
                group[i]=1
            else:
                group[i]+=1
        groups=sorted(group.items(),key = lambda x:x[1],reverse=True)
        lists=[]
        for item in groups[:k]:
            lists.append(item[0])
        return lists
