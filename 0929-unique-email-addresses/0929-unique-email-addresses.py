class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sett=set()
        for i in emails:
            l,d=i.split('@')
            res=''
            for j in l:
                if j==".":
                    continue
                elif j=='+':
                    break
                else:
                    res+=j
            sett.add(res+'@'+d)
        return len(sett)