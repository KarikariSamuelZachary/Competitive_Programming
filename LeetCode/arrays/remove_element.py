class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        output = []

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            output.append(nums[i])

        for j in range(len(output)):
            nums[j] = output[j]

        return len(output)