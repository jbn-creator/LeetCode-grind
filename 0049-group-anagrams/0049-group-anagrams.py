class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        My idea: we neeed a hashmap to store the index of an already identified anagram (e.g {anagram1: index1, anagram2: index2}).
        
        If we find a word that happens to be an already identified anagram, we simply append it to the corresponding list with the index of that list stored in the hashmap.

        If we find a word that does not correspond to any anagram, we simply append it to our list as a single valued list and add it's index.
        """
        ans = {}
        answ = []
        ind = 0
        for word in strs:
            sortedKey = tuple(sorted(word))
            if sortedKey not in ans:
                ans[sortedKey] = ind
                answ.append([word])
                ind += 1
            else:
                answ[ans[sortedKey]].append(word)
        return answ

        