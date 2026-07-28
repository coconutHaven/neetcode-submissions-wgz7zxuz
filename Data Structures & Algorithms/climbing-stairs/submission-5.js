class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let cache = new Map()
        for (let i = 1; i <= n; i++) {
            if (i == 1) {
                cache[i] = 1
            } else if (i == 2) {
                cache[i] = 2
            } else {
                cache[i] = cache[i - 1] + cache[i - 2]
            }
        }
        return cache[n]
    }
}
