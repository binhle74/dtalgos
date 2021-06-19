class ArraySolution(object):
    def duplicate_zero(self, nums, length):
        i = 0
        while i < length - 1:
            if nums[i] == 0:
                self.shift_to_right(nums, i + 1, length)
                i += 2
            else:
                i += 1

    def shift_to_right(self, nums, start, length):
        index = length - 1
        while start <= index:
            nums[index] = nums[index - 1]
            index -= 1

    def duplicate_zero_2(self, nums):
        i = 0
        count = 0
        last = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                if i + count < length - 1:
                    count += 1
                    last = i
            i += 1

        i = length - 1 - count

        while i >= 0:
            if i <= last and nums[i] == 0:
                nums[i + count - 1] = 0 # itself
                nums[i + count] = 0 # duplicate position
                count -= 1
            else:
                nums[i + count] = nums[i]
            i -= 1

    def merge_sorted_arrays(self, nums1, m, nums2, n):
        indx1 = 0
        indx2 = 0
        indx3 = 0
        nums3 = [nums1[i] for i in range(0, m)]
        while indx3 < m and indx2 < n:
            num3 = nums3[indx3]
            num2 = nums2[indx2]
            if num3 < num2:
                nums1[indx1] = num3
                indx1 += 1
                indx3 += 1
            else:
                nums1[indx1] = num2
                indx1 += 1
                indx2 += 1
        if indx3 < m:
            while indx3 < m:
                nums1[indx1] = nums3[indx3]
                indx1 += 1
                indx3 += 1
        if indx2 < n:
            while indx2 < n:
                nums1[indx1] = nums2[indx2]
                indx1 += 1
                indx2 += 1

    def merge_sorted_arrays_v2(self, nums1, m, nums2, n):
        indx1 = m
        indx2 = n
        while indx2 > 0:
            num1 = nums1[indx1 - 1]
            num2 = nums2[indx2 - 1]
            if num2 > num1:
                nums1[indx1 + indx2 - 1] = num2
                indx2 -= 1
            else:
                nums1[indx1 + indx2 - 1] = num1
                indx1 -= 1

solution = ArraySolution()
# nums1 = [1, 2, 3, 5, 7, 0, 0, 0]
# nums2 = [2, 5, 6]
# nums1 = [4,5,6,0,0,0]
# nums2 = [1,2,3]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
# nums1 = [0]
# nums2 = [1]
solution.merge_sorted_arrays_v2(nums1, 3, nums2, 3)
print(nums1)
