"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals by the start time
        intervals.sort(key=lambda x: x.start)

        ending_times: dict[int, int] = {}

        hour: int = 0
        rooms: int = 0
        max_rooms: int = 0

        while 0 < len(intervals):
            # print(ending_times)
            start_time = intervals[0].start
            end_time = intervals[0].end

            if hour in ending_times:
                rooms -= ending_times[hour]
                ending_times.pop(hour, None)  

            if hour == start_time:
                intervals.pop(0)

                if end_time in ending_times:
                    ending_times[end_time] += 1
                else:
                    ending_times[end_time] = 1

                rooms += 1

                if max_rooms < rooms:
                    max_rooms = rooms
            else: 
                hour += 1
            
        return max_rooms
            