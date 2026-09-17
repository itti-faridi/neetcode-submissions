class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 0
            else:
                s_dict[ch] +=1
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            else:
                t_dict[ch] += 1
        if s_dict == t_dict:
            return True
        else: return False