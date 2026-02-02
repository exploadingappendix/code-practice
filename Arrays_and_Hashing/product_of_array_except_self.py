class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        print(nums)
        for i in range(len(nums)):
            temp = 0 #holds the number being taken out of num
            temp = nums[i] #appends the num at index i to the temp array
            nums.pop(i) #removes number from nums at i
            product = 1
            product = math.prod(nums)  
            ret.append(product)
            nums.insert(i,temp)
        return ret