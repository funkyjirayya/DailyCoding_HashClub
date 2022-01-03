class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={}
        res=[]
        temp=[]
        for a,b in trust:
            temp.append(a)
            if b in d:
                d[b].add(a)
            else:
                d[b]={a}
        if len(d)==0:
            return n if n==1 else -1
        l={i for i in range(1,n+1)}
        for k,v in d.items():
            s=l-{k}
            if s==v:
                res.append(k)
        if res and res[0] in temp:
            return -1
            
        return res[0] if res else -1
            
            
