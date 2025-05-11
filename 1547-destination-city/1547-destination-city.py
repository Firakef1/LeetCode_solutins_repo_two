class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_count = {}

        for path in paths:

            if path[0] not in outgoing_count:

                outgoing_count[path[0]] = 1

            else:

                outgoing_count[path[0]] += 1

            if path[1] not in outgoing_count:

                outgoing_count[path[1]] = 0

        for i in outgoing_count:

            if outgoing_count[i] == 0:
                return i