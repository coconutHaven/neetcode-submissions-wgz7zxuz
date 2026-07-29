class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    longestPalindrome(s) {
        let length = 0
        let count = {}
        for (let c of s) {
            if (c in count) {
                count[c]++
                if (count[c] >= 2) {
                    count[c] -= 2
                    length += 2
                }
            } else {
                count[c] = 1
            }
                
        }
        if (length < s.length) {
            return length + 1
        }
        return length
    }
}