class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set() #course whose reprequisites have been completely explored
        path=set() #course currently being explored
        def DFS(course:int)->bool:
            if course in path:
                return True
            if course in visited:
                return False
            path.add(course)
            # explore its prerequisites:
            for prerequisite in prerequisites_dict.get(course,[]): #a course might have no reprequisite
                # recursively call DFS on every prerequisite
                if DFS(prerequisite): #found cycle
                    return True
            path.remove(course)
            visited.add(course)
            return False


        #prerequisites[i] = [a, b] -> b is the prerequisite of a
        #maybe try to use DFS
        prerequisites_dict=dict()
        for course,prerequisite in prerequisites:
            prerequisites_dict[course]=prerequisites_dict.get(course,[]) + [prerequisite]
        
        for course in range(numCourses):
            if DFS(course):
                return False

        return True