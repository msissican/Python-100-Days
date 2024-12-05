"""
魔术方法 (magic method)
如果要把自定义对象放到set或者用作dict的键
那么必须要重写__hash__和__eq__两个魔术方法
前者用来计算对象的哈希码，后者用来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象（哈希码冲撞）
所以在哈希码相同的时候还要通过__eq__来判定对象是否相同
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        # 重写 hash 方法
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        # 重写 eq 方法, 判断两个对象是否相等
        return self.stuid == other.stuid and self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        # 使用字典赋值, 通过索引设置对象的属性值
        self.students[key] = student

    def __getitem__(self, key):
        # 获得对象属性值, 可以通过索引获得对象的属性值
        return self.students[key]


def main():
    students = set()
    students.add(Student(1001, '王大锤'))
    students.add(Student(1001, '王大锤')) # 和第一个学生重复
    students.add(Student(1001, '白元芳')) # 虽然 stuid 相同, 但 name 不同, hash 码不同
    print(len(students))
    print(students)

    stu = Student(1234, '骆昊')
    stu.gender = 'Male'

    # stu.birth = '1980-11-28' # 属性birth没有在 __slot__ 中定义, 不能动态添加
    # print(stu.name, stu.birth)

    school = School('千锋教育')
    # __setitem__ 和 __getitem__ 使 school 对象更像字典
    school[1001] = Student(1001, '王大锤') # 像字典一样, 通过索引添加值, 值是 Student 对象
    school[1002] = Student(1002, '白元芳')
    school[1003] = Student(1003, '白洁')
    print(school[1002]) # 通过 __getitem__ 获得对象
    print(school[1003])


if __name__ == '__main__':
    main()

