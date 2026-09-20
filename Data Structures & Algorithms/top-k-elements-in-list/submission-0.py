class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapcount = {}
        result=[]
        for num in nums:
            mapcount[num] = mapcount.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in mapcount.items():
            buckets[freq].append(num)
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
            if len(result) == k:
                return result
        return result



        