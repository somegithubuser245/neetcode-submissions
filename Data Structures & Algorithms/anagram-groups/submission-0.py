class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        present = {}
        for s in strs:
            hashed = self.get_hashed_str(s)
            if hashed in present:
                present[hashed].append(s)
            else:
                present[hashed] = [s]

        return list(present.values())


    def get_alph_number(self, letter: str) -> int:
        # 0 for a
        return ord(letter) - 97

    def get_hashed_str(self, raw: str):
        freq = [0] * 26
        for l in raw:
            i = self.get_alph_number(l)
            freq[i] += 1

        res_str = ""
        for i, f in enumerate(freq):
            if f == 0:
                continue
            else:
                res_str += f"{i}:{f}"

        return res_str

        


