class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        queue = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh.add( (r,c) )
                elif grid[r][c] == 2:
                    queue.append( (r,c) )

            
        minute = 0

        while True:
            getRotten = set()
            while queue:
                r,c = queue.pop(0)
                if (r-1, c) in fresh:
                    fresh.remove( (r-1, c) )
                    getRotten.add( (r-1, c) )

                if (r+1, c) in fresh:
                    fresh.remove( (r+1, c) )
                    getRotten.add( (r+1, c) )

                if (r, c-1) in fresh:
                    fresh.remove( (r, c-1) )
                    getRotten.add( (r, c-1) )

                if (r, c+1) in fresh:
                    fresh.remove( (r, c+1) )
                    getRotten.add( (r, c+1) )

            if not getRotten:
                break

            minute +=1
            queue += list(getRotten)



        return minute if len(fresh) == 0 else -1