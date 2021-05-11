'''
Author: your name
Date: 2021-05-11 21:12:05
LastEditTime: 2021-05-11 21:34:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\821.字符的最短距离.py
'''
#
# @lc app=leetcode.cn id=821 lang=python
#
# [821] 字符的最短距离
#

"""
参考：https://leetcode-cn.com/problems/shortest-distance-to-a-character/solution/821zi-fu-de-zui-duan-ju-chi-4chong-jie-fa-javascri/
思路（中心扩展法）：
从原字符串s中每个字符（中心位置i）出发，向两边同时扩展寻找字符c。最先寻找到的字符c，一定距离位置i上的字符最近
"""
# @lc code=start


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        result=[0]*len(s) # 初始化结果数组，存放数组s中每个字符到字符c的最近距离

        for i in result:
            if re

# @lc code=end
