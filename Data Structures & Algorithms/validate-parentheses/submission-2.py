class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for i in s:
            if i == '[' or i == '{' or i =='(':
                li.append(i)
            elif (i == '}' or i == ']' or i == ')') and len(li) == 0:
                return False
            elif i == ']' and li[len(li) - 1] == '[':
                li.pop()
            elif i == '}' and li[len(li) - 1] == '{':
                li.pop()
            elif i == ')' and li[len(li) - 1] == '(':
                li.pop()
            else:
                return False
            
        if len(li) == 0:
            return True
        else:
            return False
        
        