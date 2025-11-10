class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        maxH = 0

        if len(citations) == 1 and citations[0] != 0:
            return 1
        if len(citations) == 1 and citations[0] == 0:
            return 0

        print(citations)
        for i in range(len(citations)):
            freq = len(citations) - i
            if  freq >= citations[i]:
                maxH = max(citations[i], maxH)
            else:
                maxH = max(freq, maxH)
        return maxH