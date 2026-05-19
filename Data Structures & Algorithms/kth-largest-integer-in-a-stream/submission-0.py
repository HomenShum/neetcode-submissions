class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        nums = self.nums
        nums.append(val)

        return sorted(nums,reverse = True)[self.k-1]

    # [3, [1, 2, 3, 3]]
    # add 3, 5, 6, 7, 8
    # 12333
    # 123335
    # 1233356