class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            if "".join(sorted(i)) in group:
                group["".join(sorted(i))].append(i)
            else:    
                group["".join(sorted(i))]=[i]
        value=[]
        for key in group:
            value.append(group[key])
        return value
