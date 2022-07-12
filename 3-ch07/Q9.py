class Solution(object):
    def threeSum(self, nums):
        
        result = []
        nums.sort()  #중복제거를 간소화 시키기 위해 정렬
        for i in range(len(nums) - 2):
            #중복인 경우 건너띄고 다음으로 넘어감
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, len(nums) - 1):
                #중복인 경우 건너띄고 다음으로 넘어감
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                for k in range(j + 1, len(nums)):
                    #중복인 경우 건너띄고 다음으로 넘어감
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                        
                    #세 개의 수 합
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result

class Solution(object):
    def threeSum(self, nums):
        
        result = []
        nums.sort()   #중복제거 간소화 하기 위해 정렬
        
        for i in range(len(nums)-2):
            #중복 일 경우 건너 뜀
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    #정답에 중복이 들어가면 X => 중복처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    #정답일 경우 투 포인터 이동
                    left += 1
                    right -= 1
                    
        return result
