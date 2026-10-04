class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zerocount = 0

        for n in nums:
            if n == 0:
                zerocount += 1
            else:
                product *= n

        if zerocount >= 2:
            return [0] * len(nums)

        output = []

        for n in nums:
            if zerocount == 1:
                if n == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(product // n)

        return output
