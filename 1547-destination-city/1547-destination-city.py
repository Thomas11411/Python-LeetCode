class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_paths = dict(paths)
        return list(set(all_paths.values()) - set(all_paths.keys()))[0]