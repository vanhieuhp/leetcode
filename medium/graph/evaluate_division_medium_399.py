# from typing import List
#
#
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         print("Test")
#         result = []
#         visited = defaultdict()
#         for i in range(len(equations)):
#             e = equations[i]
#             visited[e[0]][e[1]] = values[i]
#
# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
# queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
#
# res = Solution().calcEquation(equations, values, queries)
# print(res)
