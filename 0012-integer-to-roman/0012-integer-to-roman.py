import math
class Solution:
    def intToRoman(self, num: int) -> str:
        val = { 1: 'I', 4: 'IV', 5:'V', 9: 'IX',10:'X', 40: 'XL', 50:'L', 90: 'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        answ=""
        
        for i in range(len(numbers)):
            occurence = num // numbers[i]
            if occurence > 0:
                answ += (occurence * val[numbers[i]])
                num = num % numbers[i]
        return answ


            




            