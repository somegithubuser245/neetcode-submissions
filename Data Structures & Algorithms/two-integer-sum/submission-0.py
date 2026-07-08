class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # problem: indicies...
        # need to keep track of indicies
        # as well as account for duplicate numbers

        index_dict = {num: i for i, num in enumerate(nums)}
        for current_i, num in enumerate(nums):
            f = target - num
            f_i = index_dict.get(f)
            if not f_i:
                continue
            elif f_i == current_i:
                continue
            else:
                return [current_i, f_i]
            
            