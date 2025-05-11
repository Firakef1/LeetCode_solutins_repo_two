class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for i in s:

            try:

                t.index(i)

                if s.count(i) != t.count(i):

                    return False

            except ValueError:

                return False
        
        for i in t:

            try:

                s.index(i)

                
            
            except ValueError:

                return False
        
        return True
        