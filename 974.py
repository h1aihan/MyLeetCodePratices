from typing import List
# Subarray Sums Divisible by K
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
'''
Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

class Solution:
    # O(n) where n = len(A)
    '''
    note: for an array A[a1, a2, ... , ai, ... aj]
    the sum(ai, ... aj) = q * K + r  (quotient * K + remainder) 
    q * K + r is divisable by K if r = 0
    notice 
    sum(ai, ..., aj) = sum (a0, ... , aj) - sum(a0, ..., ai)
                 = qj * K + rj - (qi * K + ri)
                 = (qj - qi) * K + rj - ri 
                 the above is divisable by K if rj-ri=0 , when rj == ri 
    thus we can find remainder of each cumulative sum from 0 to 1, store in the dictionary, 
    if we find a remainder exists in the dictionary,
    that means rj is equal to some ri 
    the key of dic means ri which is equal to rj(same key), the value is the number of ri ==rj which is the number of  sub array that can be divisable by k,
    so we can add the amount to answer.
    Why we need d = {0: 1} ?
    Consider sum(i, j) % k == 0 and i == 0
    which means sum(0, j) % k == 0 and should count into the answer
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        current_sum = 0 
        sum_mod_dic = {0:1}
        ans = 0
        for a in A:
            current_sum += a
            current_mod = current_sum % K
            if current_mod not in sum_mod_dic:
                sum_mod_dic[current_mod] = 1
            else:
                ans += sum_mod_dic[current_mod]
                sum_mod_dic[current_mod] += 1
        return ans


'''
Question Type: Array, Math: mod operation 
Question Difficulty: Medium/Hard
'''