from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()
        index = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)


        while radiant_queue and dire_queue:
            d = dire_queue.popleft()
            r = radiant_queue.popleft()

            if r < d:
                radiant_queue.append(index)
            else:
                dire_queue.append(index)
            index = index + 1

        return "Radiant" if radiant_queue else "Dire"

senate = "DDRRR"
res = Solution().predictPartyVictory(senate)
print(res)
