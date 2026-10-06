class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        

        while (i != j):
            #if i + j < sum, then iterate j down... If i + j > sum, then iterate i down
            if (numbers[i] + numbers[j] == target):
                return [i+1,j+1]
            elif (numbers[i] + numbers[j] > target):
                j -= 1
            elif (numbers[i] + numbers[j] < target):
                i += 1
 