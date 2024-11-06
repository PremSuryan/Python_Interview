"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

"""
class Solution:
    def makeFancyString(self, s: str) -> str:
        new_str = []
        count = 1  # Start with one occurrence of the first character

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  # Reset the count for a new character

            if count < 3:  # Only append if less than 3 consecutive characters
                new_str.append(s[i])

        return s[0] + ''.join(new_str)  # Add the first character separately
