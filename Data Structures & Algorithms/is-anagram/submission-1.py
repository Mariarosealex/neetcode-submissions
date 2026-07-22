class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        if len(s)!=len(t):
            return False
        for letter in s:
            if letter not in seen:
                seen[letter]=1
            else:
                seen[letter]+=1
        for word in t:
            if word in seen:
                seen[word]-=1
            else:
                return False
        for key in seen:
            if seen[key]<0:
                return False
        return True