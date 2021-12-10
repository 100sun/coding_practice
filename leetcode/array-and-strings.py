from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}  # alphabet: latest_index
        max_length = start = 0
        for i, c in enumerate(s):
            print(c, start, used)
            if c in used and start <= used[c]:
                start = used[c] + 1  # disregard prev occurrence
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length


if __name__ == '__main__':
    test = Solution()
    # print(test.twoSum(nums=[3, 3], target=6))
    # print(test.threeSum(nums=[-5, 0, -2, 3, -2, 1, 1, 3, 0, -5, 3, 3, 0, -1]))
    # print(test.lengthOfLongestSubstring(s="abcabcbb"), 3)
    # print(test.lengthOfLongestSubstring(s="bbbbb"), 1)
    # print(test.lengthOfLongestSubstring(s=""), 0)
    # print(test.lengthOfLongestSubstring(s="pwwkew"), 3)
    # print(test.lengthOfLongestSubstring(s=" "), 1)
    # print(test.lengthOfLongestSubstring(s="aab"), 2)
    print(test.lengthOfLongestSubstring(s="dvdf"), 3)
    # print(test.lengthOfLongestSubstring(s="aab"), 2)
    # print(test.lengthOfLongestSubstring(s="aab"), 2)
