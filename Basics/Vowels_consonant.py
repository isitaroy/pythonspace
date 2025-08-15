from typing import Tuple

class Solution:
    def str_vowelsConsonant(self, str1:str)->Tuple[int, int]:
        count_vowels = 0
        count_consonant = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
        for char in str1:
            if char.isalpha():
                if char in vowels:
                    count_vowels+=1
                else:
                    count_consonant+=1
        return count_vowels, count_consonant


if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string \n")
    vowels, consonant = sol.str_vowelsConsonant(str1)
    print(vowels)
    print(consonant)