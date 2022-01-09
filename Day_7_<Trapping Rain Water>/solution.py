class Solution:
    def trap(self, height: List[int]) -> int:
        lm,rm=0,0
        l=len(height)
        ct=0
        rml=[0]*l
        rml[l-1] = height[l-1]
        for i in range(l-2,-1,-1):
            rml[i] = max(height[i],rml[i+1])

        for i in range(len(height)):
            lm=max(height[i],lm)
            if min(lm,rml[i])-height[i]<0:
                rm=0
            else:
                ct+=min(lm,rml[i])-height[i]
                rm=0
        return ct
            
            
        
