# @type of num: unsigned integer
# @return type: unsigned integer


class Solution:
    def convert_int_to_bits(self, num):
        bin_str = ""
        while num != 0:
            remainder = num%2
            bin_str += str(remainder)
            num = num//2
        return bin_str[::-1]

    def convert_decimal_to_bits_and_reversed(self, num):
        bin_str = ""
        while num != 0:
            remainder = num%2
            bin_str += str(remainder)
            num = num//2
        return int(bin_str)

    def convert_int_to_bin(self, num):
        mixin = 1
        int_num = 0
        num = str(num)
        for itm in num[::-1]:
            int_num += int(itm)*mixin
            mixin *= 2

        return int_num


    def reverseBits(self, num: int) -> int:
    	# write your awesome code here
        reversed_binary_converted_num = self.convert_decimal_to_bits_and_reversed(num)
        decimal_conv_num = self.convert_int_to_bin(reversed_binary_converted_num)

        return decimal_conv_num





s = Solution()

r = s.reverseBits(6)
print(r)
