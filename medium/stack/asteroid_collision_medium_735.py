from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                     stack.pop()
                break                
            else:
                stack.append(ast)
        return stack

asteroids = [-2,-1,1,2]
res = Solution().asteroidCollision(asteroids)
print(res)