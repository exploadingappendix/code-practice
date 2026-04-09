class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        arr = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        length = len(columnTitle) - 1
        res = 0
        i = 0
        while i != length:
            val = arr.get(columnTitle[i])
            print(f"before adding to result. val is {val}")
            print(f"before adding to result. res is {res}")
            res = (res + val) * 26
            print(f"after adding to result. res is {res}")
            print(f"before incrementing i: i is {i}")
            i += 1
            print(f"After incrementing i: i is {i}")
        val = arr.get(columnTitle[i])
        res += val
        return res




# Optimized Solution
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        # Read left to right like normal positional numbers.
        for ch in columnTitle:
            # Shift existing value one base-26 place to the left,
            # then add current letter value (A=1 ... Z=26).
            ans = ans * 26 + (ord(ch) - ord('A') + 1)

        return ans

# Intuition
# This is a positional number system problem, exactly like decimal and binary. In decimal, 321 means 3*10^2 + 2*10^1 + 1*10^0. In binary, 1010 means 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0. Excel columns follow the same idea but with base 26 and letters: A=1, B=2, ..., Z=26.

# For example, CBA becomes 3, 2, 1, so value is:
# 3*26^2 + 2*26^1 + 1*26^0.

# The left-to-right update ans = ans*26 + value is just a compact way to build that positional value step by step.

# Approach
# Initialize ans = 0.
# Traverse each character from left to right.
# Convert character to number:
# A -> 1, B -> 2, ..., Z -> 26.
# Update running answer:
# ans = ans * 26 + currentValue.
# Return ans.