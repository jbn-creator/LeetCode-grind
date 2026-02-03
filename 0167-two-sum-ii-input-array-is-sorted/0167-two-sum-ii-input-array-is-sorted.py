class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, (len(numbers) - 1)
        # if (numbers[l] + numbers[r]) == target:
        #     return [1, 2]
        # while r < (len(numbers) - 1) and (numbers[l] + numbers[r + 1]) <= target:
        #     r += 1
        # while (l + 1) < r and (numbers[l + 1] + numbers[r]) <= target:
        #     l += 1 
        while True:
            if (numbers[r] + numbers[l]) < target and (l + 1) < r:
                l += 1
            elif (numbers[r] + numbers[l]) > target and l <(r - 1):
                r -= 1
            else:
                break
        return [(l + 1), (r + 1)] 
