class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstpointer = 0
        lastpointer = len(numbers) - 1
        while firstpointer < lastpointer:
            if numbers[lastpointer] + numbers[firstpointer] > target :
                lastpointer -= 1
            elif numbers[lastpointer] + numbers[firstpointer] == target:
                return [numbers[firstpointer], numbers[lastpointer]]
            elif numbers[lastpointer] + numbers[firstpointer] < target:
                firstpointer += 1
        