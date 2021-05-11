'''
Author: your name
Date: 2021-05-11 21:12:05
LastEditTime: 2021-05-11 21:22:01
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
从原字符串s中每个字符（位置i）出发，向两边扩展寻找字符c，最先寻找到字符c的位置一定距离位置i上的字符最近
"""
# @lc code=start
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
# @lc code=end

