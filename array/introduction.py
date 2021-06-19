def find_max_consecutive_ones(nums):
    max = 0
    count = 0
    for num in nums:
        if num == 1:
            count = count + 1
            if count > max:
                max = count
        else:
            count = 0
    return max

# max_consecutive_ones = find_max_consecutive_ones([1,0,1,1,0,1])
# print(max_consecutive_ones)

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sorted_squares(nums):
    left, right = 0, len(nums) - 1
    result = [0 for num in nums]
    index = len(nums) - 1
    while(index >= 0):
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] * nums[left]
            left = left + 1
        else:
            result[index] = nums[right] * nums[right]
            right = right - 1
        index = index - 1
    return result

sorted_squares = sorted_squares([-7,-3,2,3,11])
print(sorted_squares)

