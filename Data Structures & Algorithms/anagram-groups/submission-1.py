class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # first we gotta find anagrams for each list of string
        groupings = {}

        for s in strs:
            if tuple(sorted(s)) in groupings:
                # then we can get the indice via groupings[sorted(s)]
                # and if we save a list of each indice for the sorted(s)
                # then we can append a nested list with the list of anagrams given the indice of strs
                groupings[tuple(sorted(s))].append(s)
            else:
                groupings[tuple(sorted(s))] = [s]

        return list(groupings.values())