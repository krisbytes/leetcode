from ast import List


class Solution:
    def maximumWealth(self, accounts: List[List/8[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))
        return max_wealth
