#
# @lc app=leetcode.cn id=989 lang=python
#
# [989] 数组形式的整数加法
#

"""
初步思路：
1.先排除异常情况
2.将数组变成对应数字，加上一个数后，将相加结果变回数组
"""
# @lc code=start


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int] 待加数字的数组
        :type k: int 所加的数字
        :rtype: List[int] 加数字后的数组
        """
        sum = 0
        for i in range(len(num)):
            sum += num[i]*10*(len-i)

            

            # @lc code=end
