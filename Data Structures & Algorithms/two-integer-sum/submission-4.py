class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #avoid nested loops
        seen = {}
        for i in range(len(nums)):
            # is target - num in seen
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
            
                
                
