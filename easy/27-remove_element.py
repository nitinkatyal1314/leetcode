class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = -1

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1
