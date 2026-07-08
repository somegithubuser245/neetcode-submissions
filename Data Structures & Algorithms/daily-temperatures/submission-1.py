class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        
        temps_length = len(temperatures)
        last_low = 0
        
        result = [0 for _ in range(temps_length)]

        for index in range(temps_length - 1):
            i_next = index + 1

            c_temp = temperatures[index]
            n_temp = temperatures[i_next]

            if c_temp < n_temp:
                result[index] = 1
                while len(temp_stack) > 0:
                    l_temp, l_index = temp_stack[-1]
                    if l_temp < n_temp:
                        result[l_index] = i_next - l_index
                        temp_stack.pop()
                    else:
                        break
            else:
                temp_stack.append((c_temp, index))
                last_low = n_temp

        print(temp_stack)
        print(result)
                


        return result

        
