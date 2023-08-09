class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minSize = 200
        
        for i in range(0, len(strs)) :
            if len(strs[i]) < minSize :
                minSize = len(strs[i])
        
        res = ""
        for i in range(0, minSize) :
            buff = ""
            for j in range(0, len(strs)) :
                if j != 0 and strs[j][i] != buff :
                    return res
                else :
                    buff = strs[j][i]
            res += buff
        
        return res