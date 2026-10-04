class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n != 0:
                product *= n
        output = []
        for n in nums:
            if 0 in nums and n != 0:
                output.append(0)
            elif 0 in nums and n == 0:
                output.append(product)
            else:
                output.append(product//n)
        return output

        