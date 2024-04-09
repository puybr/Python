def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    sorted_left_arr = merge_sort(left_arr)
    sorted_right_arr = merge_sort(right_arr)
    return merge(sorted_left_arr,sorted_right_arr)

def merge(left,right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result