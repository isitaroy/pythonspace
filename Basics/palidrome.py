from typing import Tuple

class Solution:
    def str_palidrome(self, str1:str)->bool:
        strlen = len(str1)
        for char in range(strlen // 2):
            if str1[char] != str1[strlen-1-char] :
                return False

        return True        


if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string \n")
    ispalidrome = sol.str_palidrome(str1)
    print(ispalidrome)