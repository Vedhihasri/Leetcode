class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            k=tuple(sorted(i))
            if k not in res:
                res[k]=[i] 
            else:
                res[k].append(i)
        return list(res.values())