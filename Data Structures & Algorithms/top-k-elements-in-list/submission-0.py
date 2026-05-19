class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # topk = [0] * k
        for i in nums: # nums = [1,2,2,3,3,3]
            if i in count: # if 1 is in {1:1}
                count[i] += 1 # then {1:(1+1)}, the same goes for 2, 3, etc.
            else: # count[1] = 1
                count[i] = 1

        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_count.keys())[:k]
