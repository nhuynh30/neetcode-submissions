class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded+= str(len(word))
            encoded+= "#"
            encoded+= word

        return encoded



    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        jump = ""
        while (i<len(s)):
            if s[i]=="#":
                word = ""
                add = int(jump)
                jump=""
                start = i+1
                end= start+add
                i+=add
                for j in range(start, end):
                    word+=s[j]
                res.append(word)
            else:
                jump+= s[i]
            i+=1
        return res




        

        