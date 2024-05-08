class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[n] = i



#! Two for loops
# Brute Force would be 0(n^2) time complexity

#! Notes
# Hashmap is mapped val: index

