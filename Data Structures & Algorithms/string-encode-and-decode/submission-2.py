class Solution:
    # self.chars = ["!", "@", "#", "$", "%", "^"]

    # def get_char_by_word_length(length: int)
    #     index = length % chars

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        delimeter = "#"
        for index in range(len(strs)):
            word = strs[index]
            appendix = delimeter + str(len(word)) + delimeter + word
            output_str += appendix

        return output_str

    def decode(self, s: str) -> List[str]:
        letters_counter = 0
        delimeter_index = 0
        delimeters_length = 0
        words = []
        
        while letters_counter < len(s) - delimeters_length:
            if s[delimeter_index] == "#":
                number_index = delimeter_index + 1
                number_str = ""
                while s[number_index] != "#":
                    number_str += s[number_index]
                    number_index += 1

                letters_length = int(number_str)
                word = ""
                first_letter_index = number_index + 1

                for j in range(letters_length):
                    char = s[first_letter_index + j]
                    word += char
                    letters_counter += 1

                words.append(word)

                delimeter_index = first_letter_index + letters_length
                delimeters_length += len(number_str) + 2

        return words


