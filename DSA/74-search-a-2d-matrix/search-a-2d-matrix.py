class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
                return False
        gg= []
        for i in range(len(matrix)):
            if target <= matrix[i][-1] and target>= matrix[i][0]:
                gg = matrix[i]
        if gg == []:
            return False
        low , high = 0, len(gg)-1
        while low <= high:
            mid = low + (high-low)// 2

            if gg[mid] == target:
                return True
            elif gg[mid] < target:
                low = mid +1
            else:
                high = mid -1

        return False


            
