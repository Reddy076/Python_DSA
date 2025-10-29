class Solution:
    def printNum(self,name,count,N):
        if(count==N):
            return
        print(name)
        
        self.printNum(name,count+1,N)



if __name__ == "__main__":
    
    sol=Solution()
    N=5
    name='red'
    sol.printNum(name,0,N)