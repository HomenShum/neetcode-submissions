"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        count = 0
        res = 0

        s = 0
        e = 0

        for i in range(len(intervals)):
            if start[s] < end[e]:
                count += 1
                s += 1
                # can we early return? yes, when all start value depletes
                if s == len(start):
                    res = max(res, count)
                    return res
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res