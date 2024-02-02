class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0 ,len(pairs) - 1)

    def mergeSortHelper(self, pairs, s, e):
        if e-s + 1 <= 1:
            return pairs

        m = ( s + e) // 2

        self.mergeSortHelper(pairs,s, m)
        self.mergeSortHelper(pairs,m+1, e)
        self.merge(pairs,s,m,e)

        return pairs

    def merge(self,arr,s,m,e):
        left = arr[s: m+1]
        right = arr[m+1: e +1]
        i,j,k = s,0,0

        while j < len(left) and k < len(right):
            if left[j].key <= right[k].key:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1

        while j <len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        while k <len(right):
            arr[i] = right[k]
            k += 1
            i += 1
