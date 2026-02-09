class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # breaks out of the for loop. 
                #Logically, if the first number is greater than 0, then there is no solution

            if i > 0 and a == nums[i - 1]:
                continue #continue skips current interation i and a
                # logically, if the current value is the same as the previous one
                # then skip the current interations loop

            l, r = i + 1, len(nums) - 1 #sets up the pointers
            #l = i + 1 and r = len(nums) - 1
            while l < r: #always in 2 pointers, the left should always be less
                #than the right
                threeSum = a + nums[l] + nums[r] #checks sum of the 3 nums
                if threeSum > 0: #if the current sum is larger than 0
                    #move the right pointer to decrease the sum
                    r -= 1
                elif threeSum < 0: #if the current sum is smaller than 0
                    #move the left pointer to increase the sum
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) #else (if sum is 0)
                    l += 1 #move left pointer to next index for next loop iteration
                    while nums[l] == nums[l - 1] and l < r: #if the current number at the current index
                                                            #is the same as the previous number
                        l += 1 #then increment left to move over
                        #logically because the copid number would return the same solution so 
                        #we skip it

        return res