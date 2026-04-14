class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSum = {} # initialise

        for i, n in enumerate(nums): #enumerate : key, value

            if (target - n) in prevSum: # difference already found

                # key of difference, key of pair
                return [prevSum[target - n], i]  
            
            else:
                prevSum[n] = i # add key value pair

                