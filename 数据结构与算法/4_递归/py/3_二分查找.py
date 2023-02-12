def binary_search(data,target,left,right):
    '''
    二分查找（p100），递归的。
    用于在一个含有n个元素的有序序列中有效的定位目标值。
    :param data:待查找的数据序列，该序列是有序的。
    :param target:要查找的目标元素的值
    :param left:用于划分数据序列的左端
    :param right:用于划分数据序列的右端
    :return:若找到了，返回True，否则，返回False
    '''
    if left>right:
        return False
    else:
        mid = (left+right)//2
        if target == data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,left,right-1)
        else:
            return binary_search(data.data, target, left+1, right)

data=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
print(binary_search(data,9,0,len(data)-1))