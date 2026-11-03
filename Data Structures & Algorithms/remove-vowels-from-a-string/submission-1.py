class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        output_str = ""
        for c in s:
            if c not in vowels:
                output_str += c
                
        return output_str


