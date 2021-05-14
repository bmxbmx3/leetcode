'''
Author: your name
Date: 2021-05-14 22:46:42
LastEditTime: 2021-05-14 22:49:45
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
        辅助栈法
        result存由内向外剥离嵌套括号并转换的字符串，multi

        :type s: str
        :rtype: str
        """
# @lc code=end

