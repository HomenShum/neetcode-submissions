class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import heapq
        heapq.heapify(nums)
        count = 0
        for i in range(len(nums)):
            
            if target != nums[0]:
                heapq.heappop(nums)
            else:
                return count
            
            count += 1
        return -1