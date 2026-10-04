class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        output = []
        for n in nums:
            output.append(product/n)
        return output

        