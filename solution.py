class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash1={}
        hash2={}
        l=[]
        for i in range(len(list1)):
            if list1[i] in list2:  
                index=list2.index(list1[i])
                hash1[list1[i]]=i+index
    
        if len(hash1)==1:
            return [k for k,v in hash1.items()]
        else:
            for k,v in sorted(hash1.items()):
                best_key = min(hash1, key=hash1.get)
                best_value=hash1[best_key]
                return [k for k,v in  hash1.items() if v==best_value]
            
