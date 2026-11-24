class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        return a[::-1]==a