class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:

            lst = sorted(word)
            sortword = "".join(lst)
            if sortword in dic:
                dic[sortword].append(word)

            else:
                dic[sortword] = []
                dic[sortword].append(word)

        
        ans = []
        for word in dic:
            ans.append(dic[word])

        return ans