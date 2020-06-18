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


test_list = random.sample(range(0, 100), 20)  # [1, 100]의 구간에서 20개의 난수 생성

print(f"unsorted list: {test_list}")
bubble_sort(test_list)
print(f"sorted list: {test_list}")
