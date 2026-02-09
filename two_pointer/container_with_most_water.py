class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, len(h) - 1
        best = 0
        while l<r:
            distance = r - l
            area = distance * min(h[l], h[r])
            best = max(best, area)
            if h[l] <= h[r]:
                l+= 1
            elif h[l] > h[r]:
                r -= 1
            else:
                break
        return best
            

