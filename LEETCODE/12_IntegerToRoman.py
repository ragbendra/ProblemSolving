class Solution:
    def intToRoman(self, num: int) -> str:
        """numeral = [ 
                    (1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'),
                    (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')
                ]

        res = []

        for value, symbol in numeral:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value
        return ''.join(res)"""

        M = ['', 'M', 'MM', 'MMM'] # 0, 1000, 2000, 3000
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 0, 100, 200...900
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 0, 10, 20...90
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 0, 1, 2...9
        
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]
