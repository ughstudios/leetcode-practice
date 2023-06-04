# https://leetcode.com/problems/merge-intervals/


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # 1. Sort the intervals ascending on starting point / end ponter
    intervals.sort()
    
    # 2. Combine adjacent intervals if they overlap
    result = []
    for interval in intervals:
        # Append the interval when no intervals are recorded
        # When the last interval and the next interval to be added are disconnected, append them as a separate interval
        if not result or interval[0] > result[-1][1]: # result[-1][1] returns the last interval appended, and it's second index. So for the second iteration of the loop it would be the number 3 result[-1] returns [1, 3] and [1, 3][1] returns 3... tldr; returns the second index of the last added interval
            result.append(interval)
        else:
            # Merge the two intervals with smallest starting point and largest ending point to detect overlaps
            # (smallest starting point is results[-1][0] because it was sorted before)
            # [1, 3] & [2, 4] -> [1, 4]
            # [1, 100] & [2, 4] -> [1, 100]
            result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
    return result


input = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(input))