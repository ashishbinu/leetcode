class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashstring = defaultdict(list)
        for string in strs:
            hashstring[sum(hash(ch) for ch in string)].append(string)
        return hashstring.values()