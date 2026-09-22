class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # if nums is sorted
        #     normal b srch
        # if left of nums is sorted
        #     if target is in that range change pointer
        #     else change pointer to start at right 
        # else right of nums is sorted 
        #     if target is in that range change pointer
        #     else change pointer to start at left 

        l, r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[r]:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] >= nums[mid]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return - 1