class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        i=0
        j=0
        v=len(word1)
        s=len(word2)
        while i<v or j<s:
            if i<v:
                result.append(word1[i])
                i+=1
            if j<s:
                result.append(word2[j])
                j+=1
        return "".join(result)

            


        