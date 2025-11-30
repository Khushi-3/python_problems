# Problem: Integer into Roman
# Write your solution below

class Solution:
    def int_to_roman(self, num: int) -> str:
        symList = (
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
            ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4), ('I', 1)
        )

        res = ""
        for sym, val in symList:
            if num // val:
                count = num // val
                res += sym * count
                num = num % val

        return res


# Testing
s = Solution()
print(s.int_to_roman(3756))  # MMMDCCLVI
print(s.int_to_roman(26))    # XXVI
print(s.int_to_roman(309))   # CCCIX
