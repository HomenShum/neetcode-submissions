class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set dedupes the list, count if new len is less than old len
        if len(set(nums)) == len(nums):
            return False
        return True