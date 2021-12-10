from collections import Counter, defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = [(k, v) for k, v in Counter(s).items()]
        hmap.sort(key=lambda x: -x[1])
        freq = defaultdict(str) # defaultdict(value) : key must be unique!! so key == int, value == str
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


if __name__ == '__main__':
    s = Solution()
    for case in ["aaabbbcc", "ceabaacb"]:
        print(s.minDeletions(case), "\n")
