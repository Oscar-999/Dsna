class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i
        return



#! Two for loops
# Brute Force would be 0(n^2) time complexity

#! Notes
# Hashmap is mapped val: index
# Tc 0(n) Sc 0(n)
