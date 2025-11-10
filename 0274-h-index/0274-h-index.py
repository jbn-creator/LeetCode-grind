class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        maxH = 0

        #edge cases when we have a single element in the list
        if len(citations) == 1 and citations[0] != 0:
            return 1
        if len(citations) == 1 and citations[0] == 0:
            return 0

        for i in range(len(citations)):
            freq = len(citations) - i

            #at least h papers (citations[i]) with h citations(freq)
            if  freq >= citations[i]:
                maxH = citations[i] #since we have our list sorted every value would be a maximum
            else:
                #this else represents cases where we a higher amount of citations than we have papers, we 
                maxH = max(freq, maxH) 
        return maxH