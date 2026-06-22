class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = len(nums)
        temp = len(set(nums))
        if val == temp:
            return False
        return True
        