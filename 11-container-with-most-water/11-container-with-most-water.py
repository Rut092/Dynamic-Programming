class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        i=0
        j=len(height)-1
        while(1):
            
            a=(j-i)*min(height[i],height[j])
            if maxi<a:
                maxi=a
            if height[i]==height[j]:
                i+=1
                j-=1
            elif height[i]>height[j]:
                j-=1
            elif height[i]<height[j]:
                i+=1
                
            if j<=i:
                break
        return maxi