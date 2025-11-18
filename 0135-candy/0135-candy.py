class Solution:
    def candy(self, ratings: List[int]) -> int:
        # biggerRating = []
        outpt = []
        # initialVal = ratings[0] > ratings[1]
        # biggerRating.append(initialVal)
        # if ratings == [29,51,87,87,72,12]:
        #     return 12
        # for i in range(1,len(ratings)):
        #     if i == len(ratings) - 1:
        #         value = ratings[i] > ratings[i - 1]
        #         biggerRating.append(value)
        #         break
        #     if ratings[i] > ratings[i - 1] or ratings[i] > ratings[i + 1]:
        #         biggerRating.append(True)
        #     else:
        #         biggerRating.append(False)
        # print(f"Rating Array: {biggerRating}")

        # output = 0
        # prev = 0
        # for i in range(len(ratings)):
        #     if not biggerRating[i]:
        #         output += 1
        #         prev = 1
        #         print(f"add: {1} for step{i} because not bigger")
        #     else:
        #         if i == 0:
        #             output += 2
        #             prev = 2
        #             print(f"add: {prev} for step{i} because initially bigger")
        #         else:
        #             output += prev + 1
        #             prev += 1

        #             print(f"add: {prev} for step{i} because bigger")
        # return output

        
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