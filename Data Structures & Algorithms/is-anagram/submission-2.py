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
            if seen[word]<0:
                return False
        return True