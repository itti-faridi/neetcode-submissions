class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen_t = {}
        for ch in s:
            if ch not in seen:
                seen[ch] = 0
            seen[ch] +=1

        for ch in t:
            if ch not in seen_t:
                seen_t[ch] = 0
            seen_t[ch] +=1

        if seen == seen_t:
            return True
        else:
            return False
        