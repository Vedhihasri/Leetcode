class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)[2:]          
        b = list(a) 
        for i in range(len(b)):
            if b[i]=='1':
                b[i]='0'
            else:
                b[i]='1'
        flip="".join(b)
        return int(flip,2)