class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        above = self.getRow(rowIndex - 1)
        out = [1]
        for i in range(1,len(above)):
            out.append(above[i-1] + above[i])
        out.append(1)

        return out