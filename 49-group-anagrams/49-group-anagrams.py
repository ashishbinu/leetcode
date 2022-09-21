class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hash of character as keys
        hashmap = defaultdict(list)
        for string in strs:
            hashmap[sum(hash(ch) for ch in string)].append(string)
        return hashmap.values()
    
        # # using alaphabet array countn as string - keys
        # hashmap = defaultdict(list)
        # for string in strs:
        #     ch_arr = [0]*26
        #     for ch in string: ch_arr[ord(ch)-ord('a')] += 1
        #     hashmap[''.join(map(chr,ch_arr))].append(string)
        # return hashmap.values()
        
        # # using tuple as keys
        # hashmap = defaultdict(list)
        # for string in strs:
        #     ch_arr = [0]*26
        #     for ch in string: ch_arr[ord(ch)-ord('a')] += 1
        #     hashmap[tuple(ch_arr)].append(string)
        # return hashmap.values()
        
        
