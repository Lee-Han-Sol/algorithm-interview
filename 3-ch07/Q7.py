class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                  
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            num = target - nums[i] #i인덱스 다음 인덱스부터 끝까지 나머지 리스트에
            if num in nums[i+1:]:  #더해서 타겟이 되는 값 있는지 확인
                return [i, nums[i+1:].index(num) + (i + 1)]
