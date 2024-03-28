class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        searchset = self.store[key]
        res = ""
        l = 0
        r = len(searchset) - 1
        
        while l <= r:
            m = (l+r)//2            
            if searchset[m][1]<=timestamp:
                res = searchset[m][0]
                l = m + 1
            else:
                r = m - 1
            
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)