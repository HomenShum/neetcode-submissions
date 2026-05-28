class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find target in sorted rotated array 
        l, r = 0, len(nums)-1 
        if nums[0] == target:
            return 0

        while l <= r:
            m = (l+r) // 2 # 3 , [7 0 1 2], 
            if nums[m] == target:
                return m
            # 2. Check if the LEFT half is normally sorted
            if nums[l] <= nums[m]:
                # Is the target inside this sorted left half?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Search left
                else:
                    l = m + 1  # Search right
                    
            # 3. Otherwise, the RIGHT half must be normally sorted
            else:
                # Is the target inside this sorted right half?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Search right
                else:
                    r = m - 1  # Search left
                    
        return -1