class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        group={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in group:
                group[i]=1
            else:
                group[i]+=1
        for i in t:
            if i in group:
                group[i]=group[i]-1
            if i not in t:
                return False
        for i in group:
            if group[i]!=0:
                return False
        return True