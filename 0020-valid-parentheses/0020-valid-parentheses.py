class Solution:
    def isValid(self, s: str) -> bool:
        openClose = {'[' : ']', '{': '}', '(' : ')', ']' : 'closedBrckt', '}': 'closedBrckt', ')': 'closedBrckt'}
        stackOpen = []
        numberOpen = 0
        numberClose = 0
        for i in range(len(s)):
            if openClose[s[i]] != 'closedBrckt':
                numberOpen += 1
                stackOpen.append(s[i])
            else:
                numberClose += 1
                if stackOpen:
                    lastOpen = stackOpen.pop()
                    if openClose[lastOpen] != s[i]:
                        return False
        if stackOpen or (len(s) % 2 != 0) or (('[' not in s) and ('{' not in s) and ('(' not in s)) or numberOpen != numberClose: 
            return False
        return True
