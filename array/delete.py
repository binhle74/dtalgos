class ArrayDeletionSolution(object):
    def remove_element(self, nums, val):
        index = 0
        count = 0
        length = len(nums)
        while index < length:
            num = nums[index]
            if num == val:
                count += 1
                nums[index] = 0
            else:
                if count != 0:
                    nums[index - count] = nums[index]
                    nums[index] = 0
            index += 1
        return length - count

    def remove_element_v2(self, nums, val):
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                # Keep the next index if num is val
                index += 1
        return index

    def remove_element_v3(self, nums, val):
        length = len(nums)
        j = 0
        for i in range(length):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def remove_duplicate_element(self, nums):
        length = len(nums)
        if length <= 1: return length
        j = 1
        for i in range(2, length):
            if nums[i] != nums[i-1]: # Note for case [1,1]
                nums[j] = nums[i]
                j += 1
        return j

# [0,0,1,1,1,2,2,3,3,4]
solution = ArrayDeletionSolution()
nums = [0,0,1,1,1,2,2,3,3,4]
nums1 = [1,1]
length = solution.remove_duplicate_element(nums)
print("length=", length, "nums=", nums)