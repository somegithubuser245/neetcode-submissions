class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # simply brute-force the sum, check for the hashed last needed member
        # space constraint violated... (n * n(-1)) / 2 possible combinations
        # don't store all of the combinations actually, but only n sums of the array
        
        found_set = set()
        result_list = []
        all_set = {num: index for index, num in enumerate(nums)}


        original_list_length = len(nums)
        for i in range(original_list_length - 1):
            for j in range(i + 1, original_list_length):
                
                first_num, second_num = nums[i], nums[j]
                two_sum = first_num + second_num

                searched = (-two_sum ** 0) * two_sum
                if (
                    (index_searched := all_set.get(searched))
                    and len(set({index_searched, i, j})) > 2
                    and {first_num, second_num, searched} not in found_set
                ):
                    triplet = [first_num, second_num, searched]
                    found_set.add(frozenset(triplet))
                    result_list.append(triplet)

        return result_list
