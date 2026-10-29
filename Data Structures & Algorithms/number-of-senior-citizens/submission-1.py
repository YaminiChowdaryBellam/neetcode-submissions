class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for num in details:
            first_digit = num[11]
            second_digit = num[12]
            age = int(first_digit +second_digit)
            if age > 60:
                count += 1
        return count


