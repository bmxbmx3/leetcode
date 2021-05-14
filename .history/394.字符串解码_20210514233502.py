'''
Author: your name
Date: 2021-05-14 22:46:42
LastEditTime: 2021-05-14 23:35:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\394.字符串解码.py
'''
#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

"""
参考：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
"""

# @lc code=start


class Solution(object):
    def decodeString(self, s):
        """
        辅助栈法：

        构造一个辅助栈stack暂存转换的中间过程。

        result_str存由内向外剥离嵌套括号并转换的字符串（编码后），
        multiply为嵌套括号外的倍数计算（用于乘嵌套内的字符串）。

        由左向右逐个扫描字符串，比如'3[a2[c]]'，即编码规则为multiply[encoded_string]：

        1.当碰到数字时存入multiply，注意如果数字超过1位，将数字字符串，按位逐个乘10，相加，变为十进制的数字，
        比如'123'即(int('1')*10+int('2'))*10+int('3')=123
        2.当碰到字母时，直接放入result_str中
        3.当碰到'['时，multiply和result_str中的内容构成一对，即(multiply,result_str)作为一个整体存入辅助栈stack中，
        然后multiply和result_str清空为后续遍历做准备。
        注意这里multiply是上个'['到当前'['的字符串中的数字字符串，例如"3[a2[c]]"中的'a'，
        result_str实际是last_result_str,即上个'['到当前'['的字符串中的字母字符串（不是右侧括号中的encoded_string），
        例如"3[a2[c]]"中的'a'，或者如"3[aa2[c]]"中的aa。
        4.当碰到']'时，stack出栈一对(multiply,last_result_str)

        :type s: str
        :rtype: str
        """
# @lc code=end
