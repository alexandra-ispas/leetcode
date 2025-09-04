class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preqMap = {}
        # course -> [preq]

        for preq in prerequisites:
            course, dependency = preq
            preqMap[course] = preqMap.get(course, []) + [dependency]

        visiting = set()

        def dfs(node):
            if node in visiting:
                # cycle detected
                return False

            if node not in preqMap.keys() or len(preqMap[node]) == 0:
                return True

            visiting.add(node)

            for p in preqMap[node]:
                if not dfs(p):
                    return False

            visiting.remove(node)
            preqMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
