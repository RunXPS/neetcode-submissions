class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # for every elem in arr1
        # find it's position in arr 2
        counts = [0] * len(arr2)
        outputs: list[int] = []
        for val in arr1:
            # find the pos in arr2
            counter = 0
            while counter < len(arr2):
                if arr2[counter] == val:
                    counts[counter] += 1
                    break
                counter += 1

            # val not in the 
            if counter == len(arr2):
                outputs.append(val)

        
        outputs.sort()

        counter = len(arr2) - 1
        while counter >= 0:
            outputs = ([arr2[counter]] * counts[counter]) + outputs
            counter -= 1
        
        return outputs