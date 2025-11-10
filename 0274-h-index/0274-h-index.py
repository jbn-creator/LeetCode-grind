class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        maxH = 0

        #edge cases when we have a single element in the list
        if len(citations) == 1 and citations[0] != 0:
            return 1
        if len(citations) == 1 and citations[0] == 0:
            return 0

        #go through the sorted list
        for i in range(len(citations)):
            freq = len(citations) - i
            if  freq >= citations[i]:
                maxH = citations[i]
            else:
                maxH = max(freq, maxH)
        return maxH