from typing import Tuple

class Solution:
        
    # def Remove_Spaces(self, str1:str)->str:
    #     result = ''
    #     for char in str1:
    #         if char != ' ':
    #             result+=char
    #     return result

    def Remove_Spaces(self, str1: str) -> str:
        return str1.replace(" ", "")
    
    
if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string1 \n")
    str2 = sol.Remove_Spaces(str1)
    print(str2)
    
    # He l l o   wor l d  abis math e w