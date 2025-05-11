class Solution:
    def interpret(self, command: str) -> str:

        temp = ""

        i = 0

        while i <= len(command) - 1:

            if command[i] == "G":

                temp += command[i]
                i += 1

            elif command[i] == "(" and command[i + 1] == ")":

                
                temp += "o"
                i += 2

            else:
                temp += "al"
                i += 4

        return temp
