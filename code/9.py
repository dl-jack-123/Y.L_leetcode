
# Leetcode - 9  Palindrome Number
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# 中文意思

一連串整數，從右至左讀取要等於左至右讀取，Output = True / False

----第一個解法
範例 如果是負數:
a = ['-', '1', '2', '1']

a.reverse() = ['1', '2', '1', '-']
很明顯不會相同，由此list 特性來區分是否為 palindrome 

Space --> 2個storge + 1 個 True /False assignment --> O(N)
Time  --> O(1) 



'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        a = list(str(x))  # a = ['1', '2', '1']  
		
        a.reverse()   # list.reverse  = 倒過來
        
        return list(str(x)) == a   
		
		
