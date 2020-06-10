class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen = len(s)
        for i in range(len(t)):
            if t[i] == s[0]:
                if s == t[i:i+slen]
                    return True
        return False
        