class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i,j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            else:
                i += 1
                j -= 1
        return -1