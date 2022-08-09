class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict=[[] for i in range(numCourses)]
        indeg=[0]*numCourses

        for i in prerequisites:
            dict[i[0]].append(i[1])
            indeg[i[1]]+=1
                
        temp=[]
        for i in range(numCourses):
            if indeg[i]==0:
                temp.append(i)
        
        count=0
        while(len(temp)!=0):
            a=temp.pop(0)
            count+=1
            for i in dict[a]:
                indeg[i]-=1
                if indeg[i]==0:
                    temp.append(i)
            
        print(count)
        if count==numCourses:
            return True
        else:
            return False