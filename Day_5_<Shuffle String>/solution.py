class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d={}
        res=''
        for i in range(len(s)):
            d[indices[i]]=s[i]
        for k,v in sorted(d.items()):
            res+=v
        return m
            
