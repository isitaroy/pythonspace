class Solution:
    def Remove_duplicate_char(self, str1:str)->str:
        if not str1:
            return ''
        seen = set()
        result = ''
        for char in str1:
            if char not in seen:
                seen.add(char)
                result+=char
        return result

if __name__ == "__main__":
    sol = Solution()

    str1 = input("Enter the string\n")
    res = sol. Remove_duplicate_char(str1)
    print(res)
    
    # Helloworldabismathew