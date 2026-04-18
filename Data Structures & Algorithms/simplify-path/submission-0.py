class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = ""
        stack = []
        lst = path.split("/")
        for i in lst:
            if not i or i == ".":
                continue
            elif i=="..":
                if stack: 
                    stack.pop()
            else:
                stack.append(i)
        res = '/'+ '/'.join(stack)
        return res

        
            