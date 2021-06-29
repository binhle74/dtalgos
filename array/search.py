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

solution = Solution()
arr1 = [10,2,5,3]
arr2 = [7,1,14,11]
arr3 = [10,2,20,3]
arr4 = [-2,0,10,-19,4,6,-8]
arr5 = [0, 0]
# exist = solution.check_if_exist(arr4)
exist = solution.check_if_exist_pair_has_num(arr1, 15)
print(exist)