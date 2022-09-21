class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using tuple as keys
        hashmap = defaultdict(list)
        for string in strs:
            ch_arr = [0]*26
            for ch in string: ch_arr[ord(ch)-ord('a')] += 1
            hashmap[tuple(ch_arr)].append(string)
        return hashmap.values()
        
        
        # # using hash of character as keys
        # hashstring = defaultdict(list)
        # for string in strs:
        #     hashstring[sum(hash(ch) for ch in string)].append(string)
        # return hashstring.values()