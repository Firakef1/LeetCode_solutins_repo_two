class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):

            return -1

        p_one, p_two = 0, 0

        while p_one <= len(haystack)-1:

            if haystack[p_one] == needle[0]:
                
                p_two = p_one + 1

                if len(needle[1:]) == 0:
                    return p_one
                
                if len(needle[1:]) > len(haystack[p_two:]):

                    return -1
                
                for i in needle[1:]:

                    if i == haystack[p_two]:
                        p_two += 1
                        continue

                    p_one += 1
                    break
                else:

                    return p_one

            else:
                p_one+=1
        
        return -1