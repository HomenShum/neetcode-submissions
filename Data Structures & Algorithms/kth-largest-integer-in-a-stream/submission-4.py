import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) # 1. heapify the list 

        while len(self.nums) > k: # 2. pop the numbers, keep only top K
            heapq.heappop(self.nums) # pop pop pop 

    def add(self, val: int) -> int:
        # nums = self.nums 
        # nums.append(val)

        # heapq.heappush(self.nums, val)

        # if len(self.nums) > self.k:
        #     heapq.heappop(self.nums)

        # evenbetter
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        # return sorted(nums,reverse = True)[self.k-1]
        return self.nums[0]

    # [3, [1, 2, 3, 3]]
    # add 3, 5, 6, 7, 8
    # 12333
    # 123335
    # 1233356