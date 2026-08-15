class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        rec = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num not in rec:
                rec[num] = 1
            else:
                rec[num] += 1
        for key, v in rec.items():
            freq[v].append(key)
        answ = []
        for i in range(len(freq) - 1, 0, - 1):
            if freq[i] != []:
                for n in freq[i]:
                    answ.append(n)
                    k -= 1
                    if k == 0:
                        return answ
