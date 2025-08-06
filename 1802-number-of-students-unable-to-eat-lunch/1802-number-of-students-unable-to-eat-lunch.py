class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(sandwiches) > 0 and count < len(students):
            now = students.pop(0)
            if now == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(now)
                count += 1
        return count