class Solution:
    def calPoints(self, operations: List[str]) -> int:
     arr = []
     for operator in operations:
        if operator == '+':
            arr.append(arr[-1]+arr[-2])
        elif operator == 'D':
            arr.append(arr[-1]*2)
        elif operator == 'C':
            arr.pop()
        else: 
            arr.append(int(operator))
     return sum(arr)
