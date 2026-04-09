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