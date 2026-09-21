class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]: #the array is sorted return lefmost element
                return nums[l]
            elif nums[l] <= nums[mid]: #the left part is sorted but not the right part thus the right contains the inflection point
                l = mid + 1
            else:
                r = mid #the left is not sorted and contains inflection point

            """
            why do we not set r = mid - 1:

            in the second if statement the right part is not sorted as mid is bigger than right pointer, thus we never need to look for mid again

            in the third (else) if statement the left part is not sorted, mid is smaller than left, since mid could be the smallest element we keep it in the boundary instead of discarding it by doing r = mid - 1

            """


        