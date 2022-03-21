# Link: https://afteracademy.com/problems/roman-to-integer

# @type of s: string
# @return type: integer
class Solution:
    def romanToInt(self, s: str) -> int:
    	# write your awesome code here
        rom_int_dct = {'I':1,'V':5,
                       'X':10,'L':50,
                       'C':100,'D':500,
                       'M':1000,'IV':4,
                       'IX':9,'XL':40,
                       'XC':90,'CD':400,
                       'CM':900}
        
        res = 0
        i=0
        while i < len(s):
            if s[i:i+2] in rom_int_dct:
                res += rom_int_dct[s[i:i+2]]
                i +=2
            else:
                res += rom_int_dct[s[i]]
                i +=1
        return res