# Algorithm

# For each index i, store a list of [snap_id, value] pairs and initialize it with [0, 0]

# set(index, val): append [current_snap_id, val] to history[index]

# snap(): return current_snap_id, then increment it

# get(index, snap_id): binary search in history[index] to find the last record with record_snap_id <= snap_id, then return its value

class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]
        


# Time complexity: O(nlogn+k)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)