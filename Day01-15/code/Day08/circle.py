"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius
    def __str__(self):
        return f'{self._radius}'

    @property
    def radius(self):
        return self._radius

    """
    @property 将方法变成属性, 通过 cir.radius 调用, 不用() or _
    setter 是某个 property 属性的方法, 当给属性赋值时调用下方定义的函数. 
    -- 只有 cir.radius = a 给赋值时才会调用, 实例类的时候不会. 
    此外 property 还有 deleter 方法. 
    """
    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':  
    radius = -5
    small = Circle(radius)
    big = Circle(radius + 3)

    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))

    small.radius = -5
    big.radius = -3
