"""
多重继承 - 一个类有两个或者两个以上的父类
MRO - 方法解析顺序 - Method Resolution Order
当出现菱形继承（钻石继承）的时候，子类到底继承哪个父类的方法
Python 2.x - 深度优先搜索
Python 3.x - C3算法 - 类似于广度优先搜索
"""
class A():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        # 重写了字典的setitem, 限定key只能设置一次
        if key in self:
            raise KeyError(str(key) + ' already set')
        # return 父类的setitem 方法, 调用父类的 __setitem__
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


def main():
    print(D.mro()) # Method Resolution Order, D B C A
    # print(D.__mro__)
    D().say_hello() # D B C A 的顺序, D 会调用 C 的方法, print Hello C


    print(SetOnceDict.__mro__) # (<class '__main__.SetOnceDict'>, <class '__main__.SetOnceMappingMixin'>, <class 'dict'>, <class 'object'>)
    my_dict= SetOnceDict()  # 限制只有在指定的key不存在时才能在字典中设置键值对
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty' # 已经有了 key username, 会报 SetOnceMappingMixin() 中的错误


if __name__ == '__main__':
    main()
