class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        arr = []

        for num in nums:
            seen[num] = seen.get(num,0) + 1 #iterating the value(#of times in nums) of each number by 1
        
        #seen = {1 : 1, 2:2, 3:3}
        #need to find top k values ex: 2 should be [2,3]
        #max(seen, key = seen.get) -> returns max
        for i in range(k):
            #for each iteration, find max value, append, and then remove value
            max_val = max(seen, key=seen.get)
            arr.append(max_val)
            seen.pop(max_val)
        return arr