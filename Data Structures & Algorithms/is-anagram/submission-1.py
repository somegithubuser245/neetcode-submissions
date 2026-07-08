class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = self.get_letter_freq(s)
        d_t = self.get_letter_freq(t)
        
        if d_s != d_t:
            return False
        return True

    def get_letter_freq(self, s: str) -> dict:
        freq = {}
        for l in s:
            if l in freq:
                freq[l] += 1
            else:
                freq[l] = 1

        return freq
