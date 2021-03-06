'''
Author: your name
Date: 2021-05-10 23:12:08
LastEditTime: 2021-05-12 23:31:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\989.数组形式的整数加法.py
'''
#
# @lc app=leetcode.cn id=989 lang=python
#
# [989] 数组形式的整数加法
#

"""

"""
# @lc code=start


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        思路：
        1.先排除异常情况
        2.将数组变成对应数字，加上一个数后，将相加结果变回数组
        
        :type num: List[int] 待加数字的数组
        :type k: int 所加的数字
        :rtype: List[int] 加数字后的数组
        """

        length = len(num)

        # 排除异常情况
        if length < 1 or length > 10000:
            return num
        if k <= 0 or k > 10000:
            return num
        if length > 1 and num[0] == 0:
            return num

        # 将num数组转换为对应的数字
        sum = 0
        for i in range(length):
            if num[i] < 0 or num[i] > 9:
                return
            sum += num[i]*10**(length-i-1)  # 逐位相加，比如[1,2]即1*10^1+2*10^0=12

        sum += k  # 计算相加结果

        # 将相加结果变为数字
        result = []
        while(sum):
            result.append(sum % 10)
            sum = sum//10  # 双斜杠（//）表示地板除，即先做除法（/），然后向下取整（floor）
        result.reverse()
        return result


num = [1, 0]
k = 1
s = Solution()
result = s.addToArrayForm(num, k)
print(result)
# @lc code=end
