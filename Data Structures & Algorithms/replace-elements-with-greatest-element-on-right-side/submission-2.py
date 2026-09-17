class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx in range(len(arr)):
            if idx == len(arr) - 1:
                arr[-1] = -1
                return arr
            curr_max = max(arr[idx + 1 :])
            print(arr)
            arr[idx] = curr_max
        arr[-1] = -1
        return arr
