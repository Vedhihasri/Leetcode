class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)[2:]          
        b = list(a) 
        for i in range(len(b)):
            if b[i]=='1':
                b[i]='0'
            else:
                b[i]='1'
        flip="".join(b)
        return int(flip,2)