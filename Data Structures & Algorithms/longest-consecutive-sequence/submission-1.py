class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSize = 1
        new = set(nums)
        for n in nums:
            prev = n - 1
            if prev in new:
                continue
            else:
                currSize = 1
                curr = n + 1
                while curr in new:
                    currSize += 1
                    curr += 1
                if currSize > maxSize:
                    maxSize = currSize
        return maxSize