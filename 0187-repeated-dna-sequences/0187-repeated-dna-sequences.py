class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        i = 0
        window = s[0:10]
        value_dict = {}

        while len(window) == 10:
            window = s[i:i+10]
            if window in value_dict:
                value_dict[window] += 1

            else:

                value_dict[window] = 1

            i += 1

        key = list(value_dict.keys())
        value = list(value_dict.values())
        output = []
        for number in range(len(value)):

            if value[number] > 1:
                output.append(key[number])

        return output


                

        