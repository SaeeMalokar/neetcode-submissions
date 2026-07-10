class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        li =[]
        for i in range(len(nums)):
            if nums[i] not in li:
                li.append(nums[i])
            else:
                li.remove(nums[i]) 
        return li.pop()
        