class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque

        rec_dct = defaultdict(int)
        graph = defaultdict(list)


        for r,ing in zip(recipes,ingredients):
            rec_dct[r] = len(ing)
            for i in ing: graph[i].append(r)

        q = deque(supplies)
        recipes = set(recipes)
        ans = []

        while q:
            x = q.popleft()
            if x in recipes: ans.append(x)
            for xx in graph[x]:
                rec_dct[xx] -= 1
                if rec_dct[xx] == 0: q.append(xx)


        return ans