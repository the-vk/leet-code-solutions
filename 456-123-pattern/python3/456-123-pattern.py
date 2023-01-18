class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        peak = -math.inf
        st = []
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x < peak:
                return True
            while len(st) > 0 and x > st[-1]:
                peak = st.pop()
            st.append(x)
        return False
