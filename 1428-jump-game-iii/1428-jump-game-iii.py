class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [(arr[start], start)]
        seen = set()
        seen.add(start)
        while queue:
            x , y = queue.pop(0)
            if x + y <= len(arr) - 1:
                if arr[x + y] == 0:
                    return True
                else:
                    if x + y not in seen:
                        queue.append((arr[x + y],x + y))
                        seen.add(x + y)
            if y - x >= 0:
                if arr[y - x] == 0:
                    return True
                else:
                    if y - x not in seen:
                        queue.append((arr[y - x],y - x))
                        seen.add(y - x) 
        return False