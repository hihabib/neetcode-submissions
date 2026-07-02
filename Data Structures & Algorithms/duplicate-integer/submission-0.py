class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = {}
        for item in nums:
            if item in checked_nums:
                return True
            else:
                checked_nums[item] = True
        return False  
