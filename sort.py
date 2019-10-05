import numpy as np
import math
import time


# 冒泡排序
def bulle_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 选择排序
def selction_sort(arr):
    for i in range(len(arr) - 1):
        max_Index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[max_Index]:
                max_Index = j
        arr[i], arr[max_Index] = arr[max_Index], arr[i]
    return arr


# 插入排序
def insertion_sort(arr, ds=1):
    for i in range(ds, len(arr)):
        temp = arr[i]
        j = i - ds
        while j >= 0 and arr[j] > temp:
            arr[j + ds] = arr[j]
            j -= ds
        arr[j + ds] = temp
    return arr


# 希尔排序
def shell_sort(arr):
    ds = math.floor(len(arr) / 2)
    while ds > 0:
        arr = insertion_sort(arr, ds)
        ds = math.floor(ds / 2)
    return arr


# 归并排序
def merge_sort(arr):
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:len(arr)]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    if not isinstance(left, list):
        left = left.tolist()
    if not isinstance(right, list):
        right = right.tolist()
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 快速排序
def quick_sort(arr, left=-1, right=-1):
    if left < 0:
        left = 0
    if right < 0:
        right = len(arr) - 1
    if (left < right):
        pivot = quick(arr, left, right)
        # print(left, pivot, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr


def quick(arr, left, right):
    pivote = left
    count = pivote + 1
    index = count
    while count <= right:
        if arr[count] < arr[pivote]:
            arr[index], arr[count] = arr[count], arr[index]
            index += 1
        count += 1
    arr[pivote], arr[index - 1] = arr[index - 1], arr[pivote]
    return index


arr_lengh = 0


# 堆排序
def heap_sort(arr):
    global arr_lengh
    arr_lengh = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr_lengh -= 1
        heapify(arr, 0)
    return arr


def build_max_heap(arr):
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    lagest = i
    if left < arr_lengh and arr[lagest] < arr[left]:
        lagest = left
    if right < arr_lengh and arr[lagest] < arr[right]:
        lagest = right
    if lagest != i:
        arr[lagest], arr[i] = arr[i], arr[lagest]
        heapify(arr, lagest)


# 计数排序
def counting_sort(arr):
    pass


if __name__ == "__main__":
    arr_test = np.random.randint(100, size=10)
    print(arr_test)
    start = time.time()
    arr_test = heap_sort(arr_test)
    use_time = time.time() - start
    print("use time:", use_time)
    print(arr_test)
