class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,N = len(p),len(s)
        res = []
        if n > N: return res
        
        # we can replace these dict with array of 26 length
        freq_p = defaultdict(int)
        window = defaultdict(int) # n length string(window) in s
        
        for i in range(n):
            freq_p[p[i]] += 1
            window[s[i]] += 1
        
        is_anagram = window == freq_p
        if is_anagram: res.append(0)
            
        for j in range(n,N):
            # This is_anagram here represents if the previous window value was anagram or not
            
            i = j - n # i represents previous windows starting position
            window[s[i]] -= 1
            window[s[j]] += 1
            
            if window[s[i]]==0: del window[s[i]] # remove character from dict if value is zero
            
            
            # hashtable comparison will take O(1)
            # as max number of comparison is 26 (only lower case alphabets)
            is_anagram = (is_anagram and s[i]==s[j]) or freq_p==window
            
            if is_anagram: res.append(i+1)
                
        return res
            