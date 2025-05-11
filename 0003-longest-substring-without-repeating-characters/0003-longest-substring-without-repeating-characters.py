class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        long_sub_string = ""
        window = ""

        for i in s:

            if i in window:

                index = window.index(i)
                window = window[index+1:] + i
                continue
            
            window += i

            if len(window) > len(long_sub_string):

                long_sub_string = window
            
        return len(long_sub_string)

        