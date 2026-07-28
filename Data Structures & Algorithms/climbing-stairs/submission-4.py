class Solution:
    def climbStairs(self, n: int) -> int:

        # ways 1 = 1
        # ways 2 = ways 1 + 1 = 2 = 11, 2
        # ways 3 = ways 2 + 1 = 3 = 111, 21, 12
        # ways 4 = ways 3 + ways 2 1111, 211, 121, 22, 112
        # ways 5 = 11111, 221, 112, 2111, 1211, 

        res = {}
        for i in range(1, n + 1):
            if i == 1:
                res[1] = 1
            elif i == 2:
                res[2] = 2
            else:
                res[i] = res[i - 1] + res[i - 2]
        return res[n]
        # def dp(i):
        #     if i <= 1:
        #         return 1
        #     else:
        #         return dp(i - 1) + dp(i - 2)
        # return dp(n)
        
