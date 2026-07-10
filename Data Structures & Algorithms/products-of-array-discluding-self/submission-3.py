class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                if j == i:
                    continue 
                else:
                    count *= nums[j]
            output.append(count)
        return output 

        