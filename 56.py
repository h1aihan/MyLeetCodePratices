from typing import List
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)
        intervals.sort(key=lambda x:x[0])
        still_merging= True
        i=0
        merging_list=intervals.copy()
        merged_list=[]
        merged=0
        while (still_merging):
            if len(merging_list)==1:
                return merging_list
            if i+1>=len(merging_list):
                if i<len(merging_list):
                    merged_list.append(merging_list[i])
                if merged==0:
                    break
                else:
                    merging_list=merged_list.copy()
                    merged_list.clear()
                    merged=0
                    i=0
                    continue
            merge_sucess=self.try_merge(merging_list[i],merging_list[i+1])
            if merge_sucess:
                merged+=1
                merged_list.append(merge_sucess)
                i+=2
            else:
                merged_list.append(merging_list[i])
                i+=1
        return merged_list
    def try_merge(self, interval1, interval2):
        if interval1[1]>= interval2[0]:
            if interval1[1]> interval2[1]:
                return [interval1[0], interval1[1]]
            return [interval1[0], interval2[1]]
        else:
            return False
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        # O(n)
        # Official 
        intervals.sort(key=lambda x:x[0])
        merged_list=[intervals[0]]
        for i in intervals:
            if merged_list[-1][1] >= i[0]:
                merged_list[-1][1]= max(merged_list[-1][1],i[1])
            else:
                merged_list.append(i)
        return merged_list
'''
Question Type: Array
Question Difficulty: Medium
Taughtby: Xiaobaobao
'''