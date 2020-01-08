'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

---分析---
兩種解法:
	一、字串調換
	二、餘數存取

#1 解說

當use str(x),index互換的動作→str(x)[start index: end index: step] , 
example: 
	if a = -a :
	a=-123456
	str(a)[::-1] --> 654321-
	str(a)[::-1][:-1]--> 654321 這row 處理負號去除
	接下來轉int + 負號就是結果
	
	if a 是正數:
	str(a)[::-1] -->跟負號插不多，少一個步驟(負號去除)
	
	int 最多只能存2**31次方，為什魔不是32次方呢?Ans: 負號佔有1bit -->32-1=31
	
	
#2 解說

condition:
	1 * list 用來存放餘數
	1 * True assignment 用來判別負號
	1 * while condition 用來尋找幾位餘數
	
example:
	a = 123456 
	a%10 = 6 , 也是a的最後一位-->存入list
	以上運算式走(len(str(a)))次
	list 長這樣= [6,5,4,3,2,1]
	
	result
	對list do for 迴圈
	result = i + 10*result # 第一次 --> 6 = 6 + 10*0 ,第二次 --> 65 = 5 + 10*6,以此類推，最後也相當於 654321
	
	下一步由True assignment 來判別，True = 負號 
	
	int 最多只能存2**31次方，為什魔不是32次方呢?Ans: 負號佔有1bit -->32-1=31
'''


#1
class Solution:
    def reverse(self, x: int) -> int:
        if '-' in str(x):
            result = (- int(str(x)[::-1][:-1]))
        else:
            result = (int(str(x)[::-1]))
        if (result <= int(-2**31)) or (result >= int(2**31 -1)):
            result = 0
        return result
		
		
		
'''
#2
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        arr = [] #set up an array to store values
        f = False #used like sign to tell whether the integer is negative or not
        if x<0:
            x=-x
            f=True
        while True:
            arr.append(x%10) #get the number of each poisition
            x=x/10
            if x==0:
                break
        result = 0
        for i in arr: #restor the reverse integer
            result = i+10*result
        if f: #restore the negative num.
            result *= -1
		if (result <= int(-2**31)) or (result >= int(2**31 -1)):
            result = 0
        return result
'''