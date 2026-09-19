class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset: #start of sequence
                length = 1 #just num for now
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length) #get the longest chain each time
        return longest

