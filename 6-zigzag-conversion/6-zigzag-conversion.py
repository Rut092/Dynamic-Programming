class Solution:
    def convert(self, s: str, numRows: int) -> str:
        st=[i for i in s]
        dp=[['' for i in range(len(s))] for i in range(numRows)]
        i=0
        j=0
        if numRows==1:
            return s
        if numRows==2:
            arr=[]
            for i in range(0,len(s),2):
                arr.append(s[i])
            for i in range(1,len(s),2):
                arr.append(s[i])
            return "".join(arr)
        if numRows>2:
            while(len(st)!=0):
                if len(st)!=0:
                    a=st[0]
                    st.pop(0)
                    dp[i][j]=a
                    i+=1
                if i==numRows:
                    print(i)
                    i-=2
                    j+=1
                    while(i>=0 and len(st)!=0):
                        b=st[0]
                        st.pop(0)
                        dp[i][j]=b
                        i-=1
                        j+=1
                        if i==0:
                            break
                    i=0
            return "".join(["".join(i) for i in dp])