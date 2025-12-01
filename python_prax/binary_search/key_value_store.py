
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


tests = [
    (["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]], 
     [None, None, "happy", "happy", None, "sad"])
]


def run_time_map(data: list) -> list:
    for _data in data:
        match _data:
            case "TimeMap":
                pass
            
            case "set":
                pass

for idx, t in enumerate(tests):
    res = run_time_map(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")