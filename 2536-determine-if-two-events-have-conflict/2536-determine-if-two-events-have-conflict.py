class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """

        start_one = event1[0].split(":")
        end_one = event1[1].split(":")

        start_two = event2[0].split(":")
        end_two = event2[1].split(":")


        start_one = int("".join(start_one))
        end_one = int("".join(end_one))

        start_two = int("".join(start_two))
        end_two = int("".join(end_two))

        if start_one <= start_two and end_one >= start_two:

            return True

        elif start_two <= start_one and end_two >= start_one:

            return True
        
        else:

            return False
        