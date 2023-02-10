class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [ [0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        print(dp)
        return dp[0][n-1] >= 0