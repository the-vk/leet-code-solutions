class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
      st = []
      while pushed:
        st.append(pushed.pop(0))
        while st and st[-1] == popped[0]:
          st.pop()
          popped.pop(0)
      return len(st) == 0