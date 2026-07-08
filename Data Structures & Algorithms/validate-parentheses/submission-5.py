class Solution:
    def isValid(self, s: str) -> bool:
        preset = {
            "[": "]",
            "{": "}", 
            "(": ")"
        }

        opening_stack = []
        opening_count = 0
        closing_count = 0

        
        for element in s:
            if element in preset.keys():
                opening_count += 1
                opening_stack.append(element)
            elif opening_stack:
                last_element = opening_stack[-1]
                if element != preset.get(last_element):
                    return False
                else:
                    opening_stack.pop(-1)
                    closing_count += 1
            else:
                return False

        return closing_count == opening_count
