class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        counter = {}
        
        for a in magazine:
            if a not in counter: counter[a] = 0
            counter[a] += 1
            
        for b in ransomNote:
            if b not in counter: counter[b] = 0
            counter[b] -= 1
            if counter[b] < 0: return False
        
        return True
        
        
        