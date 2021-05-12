'''
Author: your name
Date: 2021-05-12 23:20:48
LastEditTime: 2021-05-12 23:40:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode\1381.设计一个支持增量操作的栈.py
'''
#
# @lc app=leetcode.cn id=1381 lang=python
#
# [1381] 设计一个支持增量操作的栈
#

"""
参考：https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/solution/she-ji-yi-ge-zhi-chi-zeng-liang-cao-zuo-de-zhan-by/
思考：Java的Stack类也是由数组模拟的吗？
"""
# @lc code=start


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int 栈的容量
        """

        self.stack = [0]*maxSize  # 栈初始化
        self.top = -1  # 栈顶指针

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        # 防止溢出
        length = len(self.stack)  # 获得栈的容量
        if(self.top >= length):
            print("栈的容量已满，无法继续入栈元素！")
            return

        # 入栈元素
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        """
        :rtype: int
        """

        if(self.pop == -1):
            print("栈空无法继续出栈！")
            return

        # 出栈元素
        x = self.stack[self.top]
        self.top -= 1
        return x

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        # 栈顶指针self.top从0开始计数，所以self.top+1
        min_incre_size = min(k, self.top+1)
        for i in range(min_incre_size):
            self.stack[i] += val

s=CustomStack(4)
s.push(1)
s.push(2)
p

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
