class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = defaultdict(list)
        for i in strs:
            sortS = ''.join(sorted(i))
            strDict[sortS].append(i)
        return list(strDict.values())
        