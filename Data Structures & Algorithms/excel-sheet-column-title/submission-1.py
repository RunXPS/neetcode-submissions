class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title: str = ""
        n = 26

        while columnNumber > 0:
            columnNumber -= 1
            num = columnNumber % n
            title = chr(ord('A') + num) + title
            columnNumber = ((columnNumber) // n)
        
        return title



# hex:
# 700 % 26 = 24 (> 25)
# 26