class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        pre = 0
        temp = len(heights) - 1
        while pre <temp:
            minh = min(heights[pre], heights[temp])
            area = minh * (temp - pre)
            if area > maxa:
                maxa = area
            if heights[pre] < heights[temp]:
                pre += 1
            else:
                temp -= 1
        return maxa

        