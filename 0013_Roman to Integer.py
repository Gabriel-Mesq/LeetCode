class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000 }

        n = 0
        l = len(s)
        
        for i in range(l):
            
            if (i + 1 < l) and (dict[s[i]] < dict[s[i+1]]):
                n -= dict[s[i]]
            
            else:
                n += dict[s[i]]
        
        return n