class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = {}
        for num in nums:
            if present.get(num):
                return True
            else:
                present[num] = 1

        return False