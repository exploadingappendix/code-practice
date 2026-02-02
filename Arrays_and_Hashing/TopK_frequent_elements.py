class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        ret = []
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        print(counter)
        for key, value in counter.items(): #key is the num and value is the count of that number
            freq[value].append(key)
        print(ret)
        for i in range(len(freq) - 1, 0, -1): # line range(len(freq) - 1) starts the indexing from the back of the list, 0 is the end and -1 is the decrementing steps 
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret