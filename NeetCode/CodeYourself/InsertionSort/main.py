# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = [] # Intermediate States

        for i in range(n):
            j = i - 1

            while pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
        return res
