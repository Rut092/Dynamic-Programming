class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals, key = lambda x : (x[0], x[1]))
        print(intervals)
        tempInterval = intervals.pop(0)
        for [start, end] in intervals:
            if start <= tempInterval[1]:
                tempInterval = [min(tempInterval[0], start), max(tempInterval[1], end)]
            else:
                res.append([tempInterval[0], tempInterval[1]])
                tempInterval = [start, end]
        res.append(tempInterval)
        return res