#최대 높이는 부피에 영향 주지 X
#그저 왼쪽과 오른쪽 가르는 역할!

class Solution(object):
    def trap(self, height):
        
        if not height:  #[]인 경우
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        
        while left < right: 
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            
            #더 높은 쪽을 향해 투 포인트 이동 
            #=> 높이가 최대인 지점에서 투 포인트 만남
            if max_left <= max_right:
                volume += max_left - height[left]
                left += 1
            else:
                volume += max_right - height[right]
                right -= 1
        
        return volume
