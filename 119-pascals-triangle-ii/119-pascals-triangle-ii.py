class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[]
        if (rowIndex+1)%2==1:
            for i in range(((rowIndex+1)//2)+1):
                arr.append(self.comb(rowIndex,i))
            for i in range(len(arr)-2,-1,-1):
                arr.append(arr[i])
            return arr
        else:
            for i in range(((rowIndex+1)//2)):
                arr.append(self.comb(rowIndex,i))
            return arr+arr[::-1]
                
    def comb(self,n,r):
        if n==r:
            return 1
        elif r==0:
            return 1
        elif n==r+1:
            return n
        a=n
        temp=1
        while(a>n-r):
            temp*=a
            temp/=(n-a+1)
            a-=1
        return int(temp)