class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        st = []
        for v in timeSeries:
            if st and v <= st[-1][1]:
                l = st.pop()
                st.append((l[0], v-1))
                    
            st.append((v, v + duration -1))
        res = 0
        for (s, e) in st:
            res += (e - s + 1)
        return res