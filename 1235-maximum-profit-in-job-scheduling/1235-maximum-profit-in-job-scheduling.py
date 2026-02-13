# At any job, we can either take it and jump to the next non-conflicting job, or skip it and try the next job.

# Sorting jobs by start time and using binary search avoids repeatedly scanning for the next valid job, making the solution efficient.

# Algorithm

# Combine startTime, endTime, and profit into a jobs list
# Sort jobs by startTime
# Use DFS + memoization where dp[i] is the max profit from job i onward
# For each job at index i:
# Option 1: skip the job → dp[i + 1]
# Option 2: take the job → profit[i] + dp[nextIndex] (found via binary search)
# Store and reuse results in dp to avoid recomputation
# Return dp[0]

from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)

        # jobs = [start, end, profit], sorted by start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        starts = [s for s, _, _ in jobs]

        # memo[i] = max profit achievable from jobs[i:] (bottom-up)
        memo = [0] * (n + 1)  # memo[n] = 0 base case

        def find_next_job(last_ending_time: int) -> int:
            # first index with starts[idx] >= last_ending_time
            lo, hi = 0, n - 1
            ans = n
            while lo <= hi:
                mid = (lo + hi) // 2
                if starts[mid] >= last_ending_time:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans

        for i in range(n - 1, -1, -1):
            s, e, p = jobs[i]
            next_idx = find_next_job(e)
            take = p + memo[next_idx]
            skip = memo[i + 1]
            memo[i] = max(take, skip)

        return memo[0]

        


# Let N be the length of the jobs array.
# Time complexity: O(NlogN)