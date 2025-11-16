class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=[]
        for i in word:
            res.append(i)
            if i==ch:
                res.reverse()
                break

        return (''.join(res)+word[len(res):])

        