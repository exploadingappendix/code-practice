class Solution:
    def mirriorDistance(self, n: int) -> int:
        rev = int(str(n)[::-1])
        return abs(n - rev)