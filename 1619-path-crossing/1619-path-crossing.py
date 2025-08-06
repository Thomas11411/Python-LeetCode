class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir_dict = [0,0]
        all_set = {(0,0)}
        for i in path:
            if i == "N":
                dir_dict[1] += 1
            elif i == "S":
                dir_dict[1] -= 1
            elif i == "E":
                dir_dict[0] += 1
            else:
                dir_dict[0] -= 1


            if tuple(dir_dict) in all_set:
                return True
            else:
                all_set.add(tuple(dir_dict))

        return False
