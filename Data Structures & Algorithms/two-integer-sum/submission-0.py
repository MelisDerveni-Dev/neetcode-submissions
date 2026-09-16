class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for index, i in enumerate(nums):
            diff = target - i
            if diff in numset:
                return [numset[diff], index]
            numset[i] = index