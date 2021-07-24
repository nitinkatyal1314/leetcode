class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        two_sum_indeces = []
        for index, item in enumerate(nums):
            diff_with_target = target - item
            if item in hashmap:
                two_sum_indeces = [hashmap[item], index]
                break
            else:
                hashmap[diff_with_target] = index

        return two_sum_indeces









