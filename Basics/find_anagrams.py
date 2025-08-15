class Solution:
    def AreAnagrms(self, str1:str, str2:str)->bool:
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()

        if len(str1) != len(str2):
            
            return False

        count ={}

        for char in str1:
            count[char] = count.get(char, 0)+1

        for char2 in str2:
            if char not in count:
                return False
            count[char]-=1

            if count[char]<0:
                return False

        return True

if __name__ == "__main__":
    sol = Solution()

    str1 = input("Enter the string1\n")
    str2 = input("Enter the string2\n")
    res = sol.AreAnagrms(str1, str2)
    if res:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
    
    # listen silent
