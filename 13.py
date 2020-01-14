
"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

中文題目:羅馬文字轉整數

I,V,X,L,C,D,M 分別代表不同整數
順序由右至左，如果右值大於左值 則運算式-->左-右

Example 2:
Input: "IV"
Output: 4 -->  5 - 1 

Space : 有兩個變數，且每次判斷都會更改一次--> O(2n)-> O(n)
Time  : 一個for迴圈，O(n)
"""



class Solution:
    def romanToInt(self, s: str) -> int:
		# 需要一個存值，一個存目前位置的值(用於判別是否左大於右)
        res, prev = 0, 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:            # 由右至左
            if dict[i] >= prev:
                res += dict[i]    
            else:
                res -= dict[i]     
            prev = dict[i]
        return res