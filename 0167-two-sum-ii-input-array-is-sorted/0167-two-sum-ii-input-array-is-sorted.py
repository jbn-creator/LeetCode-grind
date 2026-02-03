class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answ = []
        l, r = 0, 1
        if (numbers[l] + numbers[r]) == target:
            return [1, 2]
        while r < (len(numbers) - 1) and (numbers[l] + numbers[r + 1]) <= target:
            r += 1
        while (l + 1) < r and (numbers[l + 1] + numbers[r]) <= target:
            l += 1 
        while True:
            if (numbers[r] + numbers[l]) < target and (l + 1) < r:
                l += 1
            elif (numbers[r] + numbers[l]) > target and l <(r - 1):
                r -= 1
            else:
                break
        answ = [(l + 1), (r + 1)] 
        print(f"element no: {l + 1} is {numbers[l]} and element no: {r + 1} is {numbers[r]} sum up to {numbers[l] + numbers[r]} supposed to be {target}")
        if len(numbers) > 32:
            print(f"answer is {numbers[23]} and {numbers[31]} which adds to {numbers[23] + numbers[31]}")   
        return answ