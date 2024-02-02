# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelpers(pairs,0,len(pairs) -1)
        return pairs
    def quickSortHelpers(self,pairs, s, e):
        if e-s + 1 <= 1:
            return
        pivot = pairs[e]
        left = s

        for i in range(s,e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] =pairs[i]
                pairs [i]
                left += 1
        pairs[e] = pairs[left]
        pairs[left] = pivot
        self.quickSortHelpers(pairs,s,left -1)
        self.quickSortHelpers(pairs,left + 1, e)
