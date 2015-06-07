class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        differences = {}
        for index, n in enumerate(num, 1):
            difference_index = differences.get(n)
            if difference_index:
                return difference_index, index
            else:
                differences[target - n] = index
