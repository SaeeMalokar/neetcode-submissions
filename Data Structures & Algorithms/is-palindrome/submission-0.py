class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''
        sttrs = ''
        for i in s:
            if i.isalnum():
                strs += i.lower()
        for i in strs[::-1]:
            if i.isalnum():
                sttrs += i.lower()
        if strs == sttrs:
            return True
        return False

        