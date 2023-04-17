#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        jobs = []
        m = 0
        for i in Jobs:
            m = max(m, i.deadline)
            jobs.append([i.id, i.profit, i.deadline])
        jobs.sort(reverse=True, key=lambda x: x[1])
        job = [-1] * (m + 1)
        profit = 0
        for id, pr, dl in jobs:
            if job[dl] == -1:
                job[dl] = id
                profit += pr
            else:
                i = dl
                while i > 0 and job[i] != -1:
                    i -= 1
                if i > 0:
                    job[i] = id
                    profit += pr
        ans = 0
        for i in job:
            if i != -1:
                ans += 1
        return [ans, profit]
  
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends