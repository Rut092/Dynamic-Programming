class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        m=len(matrix)
        n=len(matrix[0])
        high=m*n-1
        mid=(high+0)//2
        print(m)
        #if m==1:
        #    matrix.append([-1])
        while(high>=low):
            if matrix[low//n][low%n]==target:
                return True
            elif matrix[high//n][high%n]==target:
                return True
            elif matrix[mid//n][mid%n]==target:
                return True
            else:
                if matrix[mid//n][mid%n]>target:
                    high=mid-1
                else:
                    low=mid+1
                mid=(low+high)//2
        return False