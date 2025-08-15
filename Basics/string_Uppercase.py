class Solution:
    def str_uppercase(self, str1:str)->str:
        result = ""
        for char in str1:
            if 'a' <= char <= 'z':
                result += chr(ord(char)-32)
            else:
                result +=char
        return result


if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string in lowercase\n ")
    str2 = sol.str_uppercase(str1)
    print(str2)