class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        for n in nums:
            prev = n - 1
            if prev not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                    maxLength = max(length, maxLength)

        return maxLength