class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph: list = [0] * 26
        counter: int = 0

        while counter < len(s):
            alph[ord(s[counter]) - ord('a')] += 1
            alph[ord(t[counter]) - ord('a')] += -1
            counter += 1
        return alph == [0] * 26