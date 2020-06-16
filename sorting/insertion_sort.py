import random


def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        for j in range(i, 0, -1):
            if unsorted_list[j-1] > unsorted_list[j]:
                unsorted_list[j-1], unsorted_list[j] = unsorted_list[j], unsorted_list[j-1]
            else:
                break


test_list = random.sample(range(0, 100), 20)

print(f"unsorted list: {test_list}")
insertion_sort(test_list)
print(f"sorted list: {test_list}")
