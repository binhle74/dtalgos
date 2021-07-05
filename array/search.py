class Solution(object):
    def check_if_exist(self, arr):
        i = 0
        exist = False
        length = len(arr)
        while i < length:
            num = arr[i]
            j = 0
            while j < length:
                if j != i and num == 2 * arr[j]:
                    exist = True
                    break
                j += 1
            if exist: break
            i += 1
        return exist

    def check_if_exist_v2(self, arr):
        possible_set = set()
        for num in arr:
            if num in possible_set:
                return True
            possible_set.add(num*2)
            if num % 2 == 0:
                possible_set.add(num/2)
        return False

    def check_if_exist_pair_has_num(self, arr, sum):
        possible_set = set()
        for num in arr:
            if num in possible_set:
                return True
            possible_set.add(sum - num)
        return False

    def valid_mountain_array(self, arr):
        length = len(arr)
        if length < 3: return False
        if length == 3:
            if arr[1] > arr[0] and arr[1] > arr[2]: return True
            else: return False

        top = False
        for i in range(1, length - 1):
            cur = arr[i]
            nxt = arr[i + 1]
            if not top:
                prev = arr[i - 1]
                if cur <= prev: return False
                if cur > nxt: top = True
                if cur == nxt: return False
            else:
                if cur <= nxt: return False

        return top

    def valid_mountain_array_v2(self, arr):
        top = 0
        length = len(arr)
        # walk up to find the top, the order must be strictly increasing
        while top < length - 1 and arr[top] < arr[top + 1]:
            top += 1

        # the top must not be start or end of array
        if top == 0 or top == length - 1: return False

        # walk down from the top, the order must be strictly increasing
        while top < length - 1 and arr[top] > arr[top + 1]:
            top += 1
        return top == length - 1

solution = Solution()
arr1 = [2, 0, 2]
exist = solution.valid_mountain_array_v2(arr1)
print(exist)