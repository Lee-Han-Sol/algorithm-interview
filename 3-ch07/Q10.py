class Solution(object):
    def arrayPairSum(self, nums):
        pair, sum = [], 0
        nums.sort()
        
        for num in nums:
            pair.append(num)
            
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum
