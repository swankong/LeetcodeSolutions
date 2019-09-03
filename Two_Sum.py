
class Solution(object):

    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1, use List methods.
        for i, v in enumerate(nums):
            try:
                j = nums[i+1:].index(target - v)
            except ValueError:
                continue
            return [i, j + i + 1]
        return [None, None]

    def twoSum_2(self, nums, target):
        """
        :param nums:
        :param target:
        :return: List[int]
        """
        # Solution 2, use hash position map (key: value of nums list, values: position of nums value)
        # Time complexity O(n)
        pos_dict = {v:i for i, v in enumerate(nums)}  # position map
        for i, v in enumerate(nums):
            res_val = target - v
            res_pos = pos_dict.get(res_val, None)
            if res_pos is not None and i != res_pos:  # the element does not exist and do not use repeated position
                return [i, res_pos]
        return [None, None]



