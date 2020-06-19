import random


def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        for j in range(i, 0, -1):
            if unsorted_list[j-1] > unsorted_list[j]:
                unsorted_list[j-1], unsorted_list[j] = unsorted_list[j], unsorted_list[j-1]
            else:
                break


def selection_sort(unsorted_list):
    for i in range(0, len(unsorted_list)-1):
        min_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


test_list = random.sample(range(0, 100), 20)  # [1, 100]의 구간에서 20개의 난수 생성

print(f"unsorted list: {test_list}")
test_list = merge_sort(test_list)
print(f"sorted list: {test_list}")
