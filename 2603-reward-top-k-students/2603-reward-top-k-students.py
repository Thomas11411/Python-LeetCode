class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        d = {}

        for id_ , rep in zip(student_id,report):
            tmp = rep.split(" ")
            pt = 0
            for t in tmp:
                if t in positive_feedback: pt += 3
                elif t in negative_feedback: pt -= 1
            
            d[id_] = pt
            
        return [i for i,j in sorted(d.items(), key = lambda x: (-x[1],x[0]))][:k]