class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            l,r=0,len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1

            return True


        self.res = []
        def dfs(i, path):
            if i>=len(s):
                self.res.append(path[:])
                return
            
            for index in range(i, len(s)):
                word = s[i:index+1]
                if isPalindrome(word):
                    path.append(word)
                    dfs(index+1, path)
                    path.pop(-1)

        dfs(0, [])
        return self.res
