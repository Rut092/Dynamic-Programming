#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        [1,2,3,4,5]
                    ^
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    # code here
    if root==None:
        return []
    ans=[]
    a=[root]
    b=[]
    counter=0
    i=0
    while 1:
        
        if counter==0:
            if len(a)==0:
                break
            if i<len(a):
                temp=a[i]
                i+=1
                
                if temp.left!=None:
                    b.append(temp.left)
                if temp.right!=None:
                    b.append(temp.right)
            
            else:
                counter=1
                ans.append(a[0].data)
                a=[]
                i=0
        else:
            if len(b)==0:
                break
            
            if i<len(b):
                temp=b[i]
                i+=1
                
                if temp.left!=None:
                    a.append(temp.left)
                if temp.right!=None:
                    a.append(temp.right)
                
            else:
                counter=0
                ans.append(b[0].data)
                b=[]
                i=0
                
    return ans

#{ 
 # Driver Code Starts
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        result = LeftView(root)
        for value in result:
            print(value,end=" ")
        print()

# } Driver Code Ends