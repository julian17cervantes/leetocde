class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            look = target - nums[i]
            if look in seen:
                return [i, seen[look]]
            seen[nums[i]] = i
        return []