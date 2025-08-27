class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        current_sum = 0
        for x in nums:
            current_sum += x
            result.append(current_sum)
        return result

