"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Keep track of the start and end of each 
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # Iterate through two pointers to check for overlapping intervals
        s, e = 0, 0

        for i in range(len(intervals)-1):
            if start[s] <= end[e]:
                s += 1
                if start[s] < end[e]:
                    return False
                e += 1
        
        return True