class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] == coordinates[0][0]:
            return not list(filter(lambda i: i[0] != coordinates[1][0]  , coordinates))
            
            
        def line_function(x,y):
            return ((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])) * (x - coordinates[0][0]) - (y - coordinates[0][1])
        
                
        return not list(filter(lambda i: line_function(i[0],i[1]) != 0 , coordinates))