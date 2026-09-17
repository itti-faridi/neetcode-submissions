class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            complement = target-nums[i]
            if complement in seen: #look for complement in key, if it is then return index-val
                return [seen[complement], i]
            else:
                #add nums[i] into previously seen dictionary
                seen[nums[i]] = i #store key(number) and value(index)

