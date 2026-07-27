class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // Create a map to store numbers and their corresponding indices
        const map = new Map();
        
        for (let i = 0; i < nums.length; i++) {
            const currentNum = nums[i];
            const complement = target - currentNum;
            
            // If the complement exists in our map, return the indices
            if (map.has(complement)) {
                return [map.get(complement), i];
            }
            
            // Otherwise, save the current number and its index to the map
            map.set(currentNum, i);
        }
        
        // Return an empty array if no solution is found
        return [];
    }
}
