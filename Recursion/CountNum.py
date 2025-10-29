class Solution:
    def printNum(self, num, count, N):
        """Recursively prints numbers from num to N"""
        if count == N:
            return
        print(num)
        
        self.printNum(num + 1, count + 1, N)


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    N = 5
    # Print numbers from 1 to N
    solution.printNum(1, 0, N)
    