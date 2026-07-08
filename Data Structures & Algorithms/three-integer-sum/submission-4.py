class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found_set = set()
        result_list = []
        all_set = {}
        for index, num in enumerate(nums):
            if all_set.get(num):
                all_set[num].add(index)
            else:
                all_set[num] = {index}


        original_list_length = len(nums)
        for i in range(original_list_length - 1):
            for j in range(i + 1, original_list_length):
                
                first_num, second_num = nums[i], nums[j]
                two_sum = first_num + second_num

                searched = (-two_sum ** 0) * two_sum
                if (
                    (index_searched := all_set.get(searched))
                    and len(all_set[searched]) - len(set({i, j}) & all_set[searched]) > 0
                    and {first_num, second_num, searched} not in found_set
                ):
                    triplet = [first_num, second_num, searched]
                    found_set.add(frozenset(triplet))
                    all_set[searched]
                    result_list.append(triplet)

        return result_list
