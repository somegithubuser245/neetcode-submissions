class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found_set = set()
        result_list = []
        all_set = {}

        for number in nums:
            if all_set.get(number):
                all_set[number] += 1
            else:
                all_set[number] = 1

        if (zeros := all_set.get(0)) and zeros > 2:
            found_set.add(frozenset({0,0,0}))
            result_list.append([0,0,0])

        original_list_length = len(all_set)
        items = list(all_set.keys())

        for i in range(original_list_length - 1):
            for j in range(i + 1, original_list_length):                
                first_num, second_num = items[i], items[j]
                searched = (first_num + second_num) * -1

                indicies_searched = all_set.get(searched)
                
                if not indicies_searched:
                    continue

                triplet = [first_num, second_num, searched]

                if (
                    (set(triplet) not in found_set) and
                    ((indicies_searched > 1) or
                    (second_num != searched and first_num != searched))
                ):
                    found_set.add(frozenset(triplet))
                    result_list.append(triplet)

        return result_list
