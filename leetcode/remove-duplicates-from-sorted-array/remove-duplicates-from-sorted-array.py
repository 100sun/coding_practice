class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0 
        if not len(nums): return length
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length+1