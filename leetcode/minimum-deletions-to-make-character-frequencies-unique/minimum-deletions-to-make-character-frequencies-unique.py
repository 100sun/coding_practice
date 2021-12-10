from collections import Counter, defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = [(k, v) for k,v in Counter(s).items()]
        hmap.sort(key=lambda x:-x[1])
        freq = defaultdict(str)
        dels = 0
        for k, v in hmap:
            if v not in freq:
                freq[v] = k
            else:
                while v in freq:
                    dels += 1
                    v -= 1
                    if v == 0:
                        break
                freq[v] = k
        return dels
                