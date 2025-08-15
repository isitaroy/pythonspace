class Solution:
    def str_lowercase(self, str1:str)->str:
        result= ""
        for char in str1:
            if  'A' <= char <='Z':
                result+= chr(ord(char)+32)
            else:
                result+=char
        return result


if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string \n")
    str2 = sol.str_lowercase(str1)
    print(str2)