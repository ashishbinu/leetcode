class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # using builtin Counter object to speed up the algorithm
        counter = Counter(magazine)
        counter.subtract(ransomNote)
        # Finds the least common element that is negative
        if counter.most_common()[-1][1] < 0: return False
        return True
        
        # counter subtraction removes negative count
        # return not Counter(ransomNote) - Counter(magazine)
        
        # # time - O(n) , space - O(n)
        # if len(ransomNote) > len(magazine): return False
        # counter = {}
        # 
        # for a in magazine:
        #     if a not in counter: counter[a] = 0
        #     counter[a] += 1
        #     
        # for b in ransomNote:
        #     if b not in counter: counter[b] = 0
        #     counter[b] -= 1
        #     if counter[b] < 0: return False
        # 
        # return True
        
        
        