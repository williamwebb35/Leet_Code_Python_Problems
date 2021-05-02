"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, ...
...and return the new string.
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        for i in s:
            if i in ['a','e','i','o','u']:
                s = s.replace(i,'')
        return(s)
