import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        i = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] not in counter.keys():
                counter[nums[i]] = 1
                print(f"this is in the not in section: {counter}")
            elif nums[i] in counter:
                counter[nums[i]] += 1
                print(f"this is in the in section: {counter}")
        print(counter)
        res = max(counter, key=counter.get)        
        return res
            
#optimized solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res