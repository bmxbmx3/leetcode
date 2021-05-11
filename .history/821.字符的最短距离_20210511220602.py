'''
Author: your name
Date: 2021-05-11 21:12:05
LastEditTime: 2021-05-11 22:05:56
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
1.排除异常情况
2.从原字符串s中每个字符（中心位置i）出发，向两边同时扩展寻找字符c。最先寻找到的字符c，一定距离位置i上的字符最近
"""
# @lc code=start


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        length = len(s)
        result = [0]*length  # 初始化结果数组，存放数组s中每个字符到字符c的最近距离

        for i in range(length):
            # 如果遍历到字符c，则跳过（最近距离为0）
            if result[i] == c:
                continue

            """  
            以当前位置i的字符为中心，向两边扩展寻找最近的字符c
            """
            left = i  # 向左寻找，下标不断减小
            right = i  # 向右寻找，下表不断增加
            min_distance = 0  # 记录最近距离（到中心字符s[i]）
            while(left >= 0 or right <= length-1):
                # 向两边同时寻找，一旦找到字符c就停止寻找
                if(s[left] == c):
                    min_distance = c-left
                    break
                if(s[right] == c):
                    min_distance = right-c
                    break

                """ 
                left（向左标志）左移，同理right（向右标志）右移
                note:
                left若为0，left-1变为-1,到下层循环时不满足外层循环条件left>=0,
                但right却可能依然满足right<length的外层循环条件，这样导致下层循环依然可以执行，
                但此时下层循环中left=-1，使得s[left]即s[-1]因找不到值而发生错误,
                故在这里设置left>0的判断。
                同理，为了保险起见，这里right<length。
                """
                if(left > 0):
                    left -= 1
                if(right < length):
                    right += 1

            r

# @lc code=end
