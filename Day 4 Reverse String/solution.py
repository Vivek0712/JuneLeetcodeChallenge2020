class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            j = len(s)-i-1
            s[i],s[j] = s[j],s[i]