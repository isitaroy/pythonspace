from typing import Tuple

class Solution:
    def countWords(self, str1:str)->int:
        words = str1.strip().split()
        return len(words)  
        
    def countWords_manual(self, str1:str)->int:
        count = 0
        for char in str1:
            if char == ' ':
                count+=1
        if len(str1.strip())==0:
            return 0
        return count+1


if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string1 \n")
    str3 = input("Enter the string2 \n")
    count = sol.countWords(str1)
    count1 = sol.countWords_manual(str3)
    print(count)
    print(count1)