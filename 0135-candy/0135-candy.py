class Solution:
    def candy(self, ratings: List[int]) -> int:

        outpt = []
        for k in range(len(ratings)):
            outpt.append(1)
        print(outpt)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                outpt[i] = outpt[i - 1] + 1
        print(outpt)
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and outpt[j] <= outpt[j + 1]:
                outpt[j] = outpt[j + 1] + 1 
        print(outpt)
        return sum(outpt)         