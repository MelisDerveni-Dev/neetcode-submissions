class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            else:
                pass
        flag = 0
        for n in nums:
            if n != 0:
                flag = 1
        if flag == 0:
            product = 0
        zerocount = 0

        for n in nums:
            if n == 0:
                zerocount +=1
        if zerocount >= 2:
            return [0] * len(nums)


        output = []
        for n in nums:
            if 0 in nums and n != 0:
                output.append(0)
            elif 0 in nums and n == 0:
                output.append(product)
            else:
                output.append(product//n)
        return output

        