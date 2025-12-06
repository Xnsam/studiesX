

def check_possibility(numCourses: int, prereq: list) -> list:
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prereq:
        preMap[crs].append(pre)
    
    visiting = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True
        
        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True
    
    for c in range(numCourses):
        if not dfs(c):
            return False
    return True
    



tests = [
    (2, [[0, 1]], True),
    (2, [[0, 1], [1, 0]], False),
    (4, [[1,0],[2,0],[3,1],[3,2]], True)
]


for idx, t in enumerate(tests):
    res = check_possibility(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")