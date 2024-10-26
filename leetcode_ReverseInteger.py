"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


"""

class Solution:
    def rev(self,x):
        num=0
        while x>0:
            num = num*10 + x%10
            x=x//10
        return num

    def reverse(self, x: int) -> int:
        if x<0:
            x=x*-1
            x=self.rev(x)
            if x>=2**31-1:
                return 0

            return x*-1

        else:
            x=self.rev(x)
            if x>=2**31-1:
                return 0
            return x

        