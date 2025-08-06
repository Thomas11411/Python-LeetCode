class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = ["type", "color", "name"]
        return sum([1 for i in items if i[keys.index(ruleKey)] == ruleValue])