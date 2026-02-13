# DSA Used: Queue / Deque (Sliding Window)

# Intuition:
# Since timestamps are monotonically increasing, we can maintain a sliding window of the last 300 seconds by removing stale hits as new ones arrive.

# Approach:

# Use a deque hit_tracker to store hit timestamps

# On hit(timestamp): append the timestamp and remove hits older than timestamp - 300

# On getHits(timestamp): remove hits older than timestamp - 300 and return deque size

class HitCounter:

    def __init__(self):
        self.hit_tracker = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_tracker.append(timestamp)
        while self.hit_tracker[0] + 300 <= self.hit_tracker[-1]:
            self.hit_tracker.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.hit_tracker and self.hit_tracker[0] + 300 <= timestamp:
            self.hit_tracker.popleft()
        return len(self.hit_tracker)

# Time Complexity:

# hit(): O(n) worst case (stale cleanup)

# getHits(): O(n) worst case (stale cleanup)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
