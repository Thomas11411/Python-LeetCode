class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        place = 0
        for i in typed:
            if i == name[place]:
                place += 1
                if len(name) == place:
                    return True
        return len(name) == place
