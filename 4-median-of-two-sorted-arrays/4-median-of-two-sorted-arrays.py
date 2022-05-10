class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        i=0
        j=0
        while(True):
            
            if i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j]:
                    arr.append(nums1[i])
                    i+=1

                elif nums1[i]>=nums2[j]:
                    arr.append(nums2[j])
                    j+=1
            else:
                if i>=len(nums1) and j<len(nums2):
                    for p in range(j,len(nums2)):
                        arr.append(nums2[p])
                    break
                elif j>=len(nums2) and i<len(nums1):
                    for p in range(i,len(nums1)):
                        arr.append(nums1[p])
                    break
                break
        if len(arr)%2==0:
            a=int(len(arr)/2)
            return (arr[a-1]+arr[a])/2
        else:
            return arr[int(len(arr)/2)]
    