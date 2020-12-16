import typing
'''
Q :    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
'''
class Solution:
    '''
    Run time: O(i*j)
    Space: O(1)
    '''
    def maximumWealth(self, accounts):
        richest_amount=0
        for i in range(len(accounts)):
            if sum(accounts[i])>richest_amount:
                richest_amount= sum(accounts[i])
        return richest_amount
    def sum_the_array(self, array):
        return sum(array)
    def maximumWealth2(self, accounts):
        return max(map(self.sum_the_array, accounts))
    def maximumWealth3(self, accounts):
        return sum(sorted(accounts, key= lambda x: sum(x),reverse=True)[0])
        
if __name__ == "__main__":
    s1 = Solution()
    print(s1.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
    print(s1.maximumWealth2([[2,8,7],[7,1,3],[1,9,5]]))
    print(s1.maximumWealth3([[2,8,7],[7,1,3],[1,9,5]]))
'''
Question Type: Array
Question Difficulty: Easy
'''