class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        sequences = []
        known = {}
        for x in nums:
            ax = (x,)
            ad = []
            for s in sequences:
                if (x >= s[-1]):
                    n = s + ax
                    self.add_if_new(ad, known, n)
            sequences += ad
            self.add_if_new(sequences, known, ax)
        return filter(lambda x: len(x) >= 2, sequences)

    def add_if_new(self, sequences, store, n):
        if not self.seen(store, n):
            sequences.append(n)
            l = store.get(n[0], [])
            l.append(n)
            store[n[0]] = l

    def seen(self, store, c):
        if c[0] not in store:
            return False
        for x in store[c[0]]:
            if x == c:
                return True
        return False