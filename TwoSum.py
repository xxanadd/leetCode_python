class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        # nums_set = set(nums)
        nums_dict = {}
        for first_index in range(len(nums)):
            nums_dict[nums[first_index]] = first_index

        for first_index in range(len(nums)):
            first_value = nums[first_index]
            if (target - first_value) in nums_dict:
                second_idx = nums_dict[target - first_value]
                if second_idx != first_index:
                    res = [first_index, second_idx]
                    break
        return res

