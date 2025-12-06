
def get_order(num_courses: int, prereq: list) -> list:
    crs_map = {i: [] for i in range(num_courses)}
    for crs, pre in prereq:
        crs_map[crs].append(pre)
    
    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        
        cycle.add(crs)
        for pre in crs_map[crs]:
            if dfs(pre) is False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True
    
    for c in range(num_courses):
        if dfs(c) is False:
            return []
    return output
    
tests = [
    (2, [[1, 0]], [0, 1]), 
    (4, [[1,0],[2,0],[3,1],[3,2]], [0, 1, 2, 3]),
    (3, [[0,1], [1, 2], [2, 0]], [])
]


for idx, t in enumerate(tests):
    res = get_order(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")