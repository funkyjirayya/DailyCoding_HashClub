class Solution:
    def validate(self,s):
        st=''
        l=s.split('@')
        if '+' in l[0]:
            index=l[0].index('+')
            l[0]=l[0][:index]
        l[0]=l[0].replace('.','')
        st+=l[0]+'@'+l[1]
        return st
        
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid=[]
        for i in range(len(emails)):
            valid.append(self.validate(emails[i]))
        print(valid)
            
        return len(set(valid))
        
