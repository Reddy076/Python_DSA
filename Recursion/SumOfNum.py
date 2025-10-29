class Solution:
    def printNum(self,N):
        if N<=1:
            return N
        return N+self.printNum(N-1)



if __name__ == "__main__":
    
    sol=Solution()
    N=5
    sum=sol.printNum(N)
    print(sum)