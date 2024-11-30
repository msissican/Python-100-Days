"""
排序 - 冒泡排序、选择排序、归并排序、快速排序
冒泡排序 - O(n ** 2)：两两比较，大的下沉
35, 97, 12, 68, 55, 73, 81, 40
35, 12, 68, 55, 73, 81, 40, [97]
12, 35, 55, 68, 73, 40, [81]
12, 35, 55, 68, 40, [73]
...
选择排序 - O(n ** 2)：每次从剩下元素中选择最小
-----------------------------------------
归并排序 - O(n * log_2 n) - 高级排序算法
35, 97, 12, 68, 55, 73, 81, 40
[35, 97, 12, 68], [55, 73, 81, 40]
[35, 97], [12, 68], [55, 73], [81, 40]
[35], [97], [12], [68], [55], [73], [81], [40]
[35, 97], [12, 68], [55, 73], [40, 81]
[12, 35, 68, 97], [40, 55, 73, 81]
[12, 35, 40, 55, 68, 73, 81, 97]
-----------------------------------------
快速排序 - 以枢轴为界将列表中的元素划分为两个部分，左边都比枢轴小，右边都比枢轴大
35, 97, 12, 68, 55, 73, 81, 40
35, 12, [40], 68, 55, 73, 81, 97
[12], 35, [40], 68, 55, 73, 81, [97]
[12], 35, [40], 55, [68], 73, 81, [97]
[12], 35, [40], 55, [68], 73, [81], [97]
"""


class Person(object):
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __gt__(self, other):
    #     return self.name > other.name

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序

    1. 选择最小的元素
    2. 交换到第一位
    3. 选择剩下的最小的元素
    4. 交换到第二位
    5. ...
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        # 选择最小的元素
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        # 交换到第一位
        items[i], items[min_index] = items[min_index], items[i]
    return items


# 函数的设计要尽量做到无副作用（不影响调用者）
# 9 1 2 3 4 5 6 7 8
# 9 2 3 4 5 6 7 8 1
# *前面的参数叫位置参数，传参时只需要对号入座即可
# *后面的参数叫命名关键字参数，传参时必须给出参数名和参数值
# *args - 可变参数 - 元组
# **kwargs - 关键字参数 - 字典
def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
    """
    冒泡排序(鸡尾酒排序)

    1. 选出最大的元素
    2. 交换到最后一位
    3. 选出剩下的最大的元素
    4. 交换到倒数第二位
    5. ...
    """
    items = origin_items[:]
    for i in range(1, len(items)):
        swapped = False
        # 选出最大的元素
        for j in range(i - 1, len(items) - i):
            if comp(items[j], items[j + 1]):
                # 交换到最后一位
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            # 选出剩下的最小的元素
            for j in range(len(items) - i - 1, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    # 交换到倒数第二位
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(items, comp=lambda x, y: x <= y):
    """
    归并排序

    1. 如果列表的元素个数 < 2，直接返回列表
    2. 选择中间元素
    3. 将列表分成两个部分
    4. 对每个部分进行排序
    5. 将排好序的两个部分合并成一个新的有序列表
    """
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    # 将排好序的两个部分合并成一个新的有序列表
    return merge(left, right, comp)


def merge(items1, items2, comp=lambda x, y: x <= y):
    """
    合并（将两个有序列表合并成一个新的有序列表）

    :param items1: 第一个有序列表
    :param items2: 第二个有序列表
    :param comp: 两个参数的比较函数，用于比较两个元素的大小
    :return: 一个新的有序列表
    """
    items = []
    index1, index2 = 0, 0
    # 将两个列表中的元素逐个比较
    while index1 < len(items1) and index2 < len(items2):
        # 如果第一个列表中的元素小于第二个列表中的元素
        if comp(items1[index1], items2[index2]):
            # 将第一个列表中的元素添加到结果列表中
            items.append(items1[index1])
            # 将第一个列表中的索引加1
            index1 += 1
        else:
            # 将第二个列表中的元素添加到结果列表中
            items.append(items2[index2])
            # 将第二个列表中的索引加1
            index2 += 1
    # 将剩下的元素添加到结果列表中
    items += items1[index1:]
    items += items2[index2:]
    # 返回结果列表
    return items

# list1 = [1,3,5,8,2,4,6,7,0]
# list = merge_sort(list1)


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    """
    快速排序，划分交换排序(partition-exchange sort)

    1. 选择基准元素
    2.  partition
        - 选择基准元素
        - 对数组进行分区
        - 将基准元素放到最终的位置
    3. 递归对左半部分和右半部分进行排序
    """
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    """
    Performs a quick sort on a list of items.

    This is a recursive function that sorts a list of items in place by partitioning
    the list into smaller sublists and sorting those sublists individually.

    :param items: The list of items to be sorted.
    :param start: The starting index of the sublist to be sorted.
    :param end: The ending index of the sublist to be sorted.
    :param comp: A comparator function that returns True if the first argument is
                 considered less than or equal to the second argument.
    """
    # Base case: if the start index is less than the end index, proceed with sorting
    if start < end:
        # Partition the list and get the position of the pivot element
        pos = _partition(items, start, end, comp)
        # Recursively sort the elements before the pivot
        _quick_sort(items, start, pos - 1, comp)
        # Recursively sort the elements after the pivot
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    """
    Partitions the list into two parts, with elements less than the pivot to the left
    and elements greater than or equal to the pivot to the right.

    :param items: The list of items to be partitioned.
    :param start: The starting index of the sublist to be partitioned.
    :param end: The ending index of the sublist to be partitioned.
    :param comp: A comparator function that returns True if the first argument is
                 considered less than the second argument.
    :return: The index position of the pivot element after partitioning.
    """
    pivot = items[end]  # Choose the last element as the pivot
    i = start - 1  # Initialize the smaller element index

    # i 的增量, 其实是小于 pivot 的数量, 最后把 pivot 放在 i 的后面
    # j 寻找到小于 pivot 的数, 往左面的 i+1 换,
    # i+1 指向大于 pivot 的数(i会追上j, i+1会选上j判断过的比key大的数)
    for j in range(start, end):
        # If the current element is smaller than the pivot
        if comp(items[j], pivot):
            i += 1  # Increment the smaller element index
            # Swap the elements at i and j
            items[i], items[j] = items[j], items[i]
    # Swap the pivot element with the element at i+1
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1  # Return the partitioning index

list1 = [3,2,1,5,6,9,8,7]
list = quick_sort(list1)


def main():
    """主函数"""
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(bubble_sort(items))
    # print(select_sort(items))
    # print(merge_sort(items))
    print(quick_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    # print(bubble_sort(items2, comp=lambda p1, p2: p1.age > p2.age))
    # print(select_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    # print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    # print(bubble_sort(items3))
    # print(bubble_sort(items3, comp=lambda x, y: len(x) > len(y)))
    # print(merge_sort(items3))
    print(merge_sort(items3))


if __name__ == '__main__':
    main()
