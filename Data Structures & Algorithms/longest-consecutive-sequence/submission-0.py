class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        for num in numset:
            if num - 1 in numset:
                continue
            count = 1
            nextval = num + 1
            while nextval in numset:
                nextval += 1
                count += 1
            if count > maxcount:
                maxcount = count
        return maxcount 


        