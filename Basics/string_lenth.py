class Solution:
    def string_length(self, str1:str)->int:
        count = 0
        for char in str1:
            count+=1
        return count

if __name__ == "__main__":
    sol = Solution()
    str1 = input("Enter the string")
    count = sol.string_length(str1)
    print(count)
