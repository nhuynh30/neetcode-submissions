class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []

        for word in strs:
            newWord = ''.join(sorted(word))
            if newWord not in dic:
                dic[newWord] = [word]
            else:
                dic[newWord].append(word)

        for word in dic:
            res.append(list(dic[word]))            

        return res
        
