class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def remove_intervals(intervals):
            intervals.sort(key=lambda x : x[1])
            # print(intervals)
            n=len(intervals)
            count=1
            prev_interval=0
            for i in range(1,n):
                if intervals[i][0]>=intervals[prev_interval][1]:
                    prev_interval=i
                    count+=1
            return n-count
        return remove_intervals(intervals)


    