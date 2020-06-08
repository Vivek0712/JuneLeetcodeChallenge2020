class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        return (x and (not(x & (x - 1))) )